from typing import Optional, List
from django.db.models import Count, Q, F, Prefetch
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.storages.dtos import *
from fb_post_v2.models import Post, Comment, Reaction, User


class PostStorageImplementation(PostStorageInterface):

    def validate_post_id(self, post_id: int):

        bool_field = Post.objects.filter(id=post_id).exists()
        return bool_field

    def create_post(self, user_id: int, post_content: str) -> int:

        post_obj = Post.objects.create(posted_by_id=user_id,
                                       content=post_content)
        return post_obj.id

    def delete_post(self,post_id: int):

        Post.objects.filter(id=post_id).delete()

    def get_user_of_post(self, post_id: int) -> int:

        post_obj = Post.objects.get(id=post_id)
        return post_obj.posted_by_id

    def get_posts_with_more_positive_reactions(self) -> List[int]:

            positive = Q(reaction__reaction__in=[
                ReactionType.THUMBS_UP.value, ReactionType.LIT.value,
                ReactionType.LOVE.value,ReactionType.HAHA.value,
                ReactionType.WOW.value
            ])
            negative = Q(reaction__reaction__in=[
                ReactionType.THUMBS_DOWN.value,
                ReactionType.SAD.value,
                ReactionType.ANGRY.value
            ])
            post_ids_list = list(Post.objects.values_list('id', flat=True)\
                .annotate(
                    positive_reactions=Count('reaction', filter=positive),
                    negative_reactions=Count('reaction', filter=negative)
                ).filter(positive_reactions__gt=F('negative_reactions'))
            )

            return post_ids_list

    def get_posts_reacted_by_user(self, user_id: int) -> List[int]:

        post_ids_list = list(
            Post.objects.values_list('id', flat=True)\
            .filter(reaction__in=Reaction.objects.filter(reacted_by_id=user_id))\
            .distinct()
        )
        return post_ids_list

    def get_post_details_dto(self, post_id: int) -> PostDetailsDto:

        queryset = Comment.objects\
            .select_related('commented_by')\
            .prefetch_related('reaction_set')
        post_obj = Post.objects\
            .filter(id=post_id)\
            .select_related('posted_by')\
            .prefetch_related(
                'reaction_set',
                Prefetch('comment_set', queryset=queryset)
            ).first()

        post_details_dto_obj = self._get_post_details_dto_obj(post_obj)

        return post_details_dto_obj

    def _get_post_details_dto_obj(self, post_obj):

        post_dto = self._convert_post_obj_to_dto(post_obj)
        comment_objs = post_obj.comment_set.all()
        comments_dto = self._convert_comment_objs_to_dto(comment_objs)
        post_reactions_objs = list(post_obj.reaction_set.all())
        comments_reactions_objs = self.get_comments_reactions_objs(comment_objs)
        reaction_objs = post_reactions_objs + comments_reactions_objs
        reactions_dto = self._convert_reaction_objs_to_dto(reaction_objs)
        user_objs = self._get_user_objs_to_comments(comment_objs)
        user_objs.add(post_obj.posted_by)
        users_dto = self._convert_user_objs_to_dtos(user_objs)
        return PostDetailsDto(
            post_dto=post_dto, comments_dto=comments_dto,
            users_dto=users_dto, reactions_dto=reactions_dto,
        )

    @staticmethod
    def _get_user_objs_to_comments(comment_objs):

        return {
            comment_obj.commented_by for comment_obj in comment_objs
        }

    def get_user_posts_details_dto(self,
        user_id: int) -> UserPostsDetailsDto:

        queryset = Comment.objects\
            .select_related('commented_by')\
            .prefetch_related('reaction_set')
        post_objs = Post.objects\
            .filter(posted_by_id=user_id)\
            .select_related('posted_by')\
            .prefetch_related(
                'reaction_set',
                Prefetch('comment_set', queryset=queryset)
            )

        user_posts_details_dto = self._get_user_posts_details_dto(post_objs)

        return user_posts_details_dto

    def _get_user_posts_details_dto(self, post_objs):

        posts_dto = self._convert_post_objs_to_dtos(post_objs)
        comments_objs = self._get_comments_objs_to_post_objs(post_objs)
        comments_dto = self._convert_comment_objs_to_dto(comments_objs)
        posts_reactions_objs = self._get_reaction_objs_to_posts(post_objs)
        comments_reactions_objs =\
            self.get_comments_reactions_objs(comments_objs)
        reactions_objs = posts_reactions_objs + comments_reactions_objs
        reactions_dto = self._convert_reaction_objs_to_dto(reactions_objs)
        user_objs = self._get_user_objs_to_posts_and_comments(
            post_objs, comments_objs)
        users_dto = self._convert_user_objs_to_dtos(user_objs)
        return UserPostsDetailsDto(
            posts_dto=posts_dto, comments_dto=comments_dto,
            reactions_dto=reactions_dto, users_dto=users_dto
        )

    def _convert_user_objs_to_dtos(self, user_objs):

        return [
            self._convert_user_obj_to_dto(user_obj)
            for user_obj in user_objs
        ]

    def _get_user_objs_to_posts_and_comments(self, post_objs, comments_objs):

        posts_user_objs = {
            post_obj.posted_by for post_obj in post_objs
        }

        comments_user_objs = self._get_user_objs_to_comments(comments_objs)

        user_objs = posts_user_objs.copy()
        user_objs.update(comments_user_objs)
        return user_objs

    @staticmethod
    def _get_reaction_objs_to_posts(post_objs):

        reaction_objs = []
        for post in post_objs:
            for reaction in post.reaction_set.all():
                reaction_objs.append(reaction)
        return reaction_objs
        
    @staticmethod
    def _get_comments_objs_to_post_objs(post_objs):

        comments_objs = []
        for post in post_objs:
            for comment in post.comment_set.all():
                comments_objs.append(comment)
        return comments_objs

    def _convert_post_objs_to_dtos(self, post_objs):

        return [
            self._convert_post_obj_to_dto(post_obj)
            for post_obj in post_objs
        ]

    def _convert_reaction_objs_to_dto(self, reaction_objs):

        reactions_dto = [
            self._convert_reaction_obj_to_dto(reaction_obj)
            for reaction_obj in reaction_objs
        ]
        return reactions_dto

    def _convert_comment_objs_to_dto(self, comment_objs):

        comments_dto = [
            self._convert_comment_obj_to_dto(comment_obj)
            for comment_obj in comment_objs
        ]
        return comments_dto

    @staticmethod
    def get_comments_reactions_objs(comment_objs):

        reaction_objs = []
        for comment in comment_objs:
            for reaction in comment.reaction_set.all():
                reaction_objs.append(reaction)
        return reaction_objs

    @staticmethod
    def _convert_user_obj_to_dto(user_obj):

        user_dto = UserDto(
            id=user_obj.id, name=user_obj.name,
            profile_pic=user_obj.profile_pic
        )
        return user_dto

    @staticmethod
    def _convert_reaction_obj_to_dto(reaction_obj):

        reaction_dto = ReactionDto(
            id=reaction_obj.id,
            comment_id=reaction_obj.comment_id,
            post_id=reaction_obj.post_id,
            reacted_by_id=reaction_obj.reacted_by_id,
            reaction=reaction_obj.reaction
        )
        return reaction_dto

    @staticmethod
    def _convert_comment_obj_to_dto(comment_obj):

        comment_dto = CommentDto(
            parent_comment_id=comment_obj.parent_comment_id,
            id=comment_obj.id, post_id=comment_obj.post_id,
            commented_by_id=comment_obj.commented_by_id,
            commented_at=comment_obj.commented_at,
            comment_content=comment_obj.content
        )
        return comment_dto

    @staticmethod
    def _convert_post_obj_to_dto(post_obj):

        post_dto = PostDto(
            id=post_obj.id, post_content=post_obj.content,
            posted_by_id=post_obj.posted_by_id,
            posted_at=post_obj.posted_at
        )
        return post_dto