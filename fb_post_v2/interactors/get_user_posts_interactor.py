from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from typing import List, Dict, Any
from collections import defaultdict
from fb_post_v2.dtos.dtos import *

class GetUserPostsInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_user_posts(self, user_id: int) -> List[Dict[str, Any]]:

        user_posts_details_dto = self.storage\
            .get_user_posts_details_dto(user_id=user_id)
        reactions_dto = user_posts_details_dto.reactions_dto
        posts_reactions_dict, posts_reactions_count_dict, comments_reactions_dict,\
            comments_reactions_count_dict = self._get_reactions_dicts(reactions_dto)
        comments_dto = user_posts_details_dto.comments_dto
        posts_comments_count_dict, comment_replies_count_dict\
            = self._get_comments_dicts(comments_dto)
        posts_reactions_dto, posts_comments_dto, comments_reactions_dto,\
            comment_replies_count_dto = self._get_post_extra_details(
                posts_reactions_dict, posts_reactions_count_dict,
                posts_comments_count_dict, comments_reactions_dict,
                comments_reactions_count_dict, comment_replies_count_dict,
                user_posts_details_dto
            )
        user_posts_complete_details_dto = self._get_user_posts_complete_details_dto(
            user_posts_details_dto, posts_reactions_dto, posts_comments_dto,
            comments_reactions_dto, comment_replies_count_dto)

        return self.presenter.get_response_for_get_user_posts_details_dto(
            user_posts_complete_details_dto=user_posts_complete_details_dto
        )



    def _get_post_extra_details(
            self, posts_reactions_dict, posts_reactions_count_dict,
            posts_comments_count_dict, comments_reactions_dict,
            comments_reactions_count_dict, comment_replies_count_dict,
            user_posts_details_dto
        ):
        posts_dto = user_posts_details_dto.posts_dto
        comments_dto = user_posts_details_dto.comments_dto
        comments_dict = self._get_comments_list_dict(comments_dto)

        post_reactions_dto = self._get_post_reactions_dto(
            posts_reactions_dict, posts_reactions_count_dict,
            posts_dto
        )
        post_comments_dto = self._get_posts_comments_count_dict(
            posts_comments_count_dict, posts_dto
        )
        comments_list = comments_dict['comments']
        comments_reactions_dto = self._get_comment_reactions_dto(
            comments_list, comments_reactions_dict,
            comments_reactions_count_dict)
        parent_comments_list = comments_dict['parent_comments']
        comment_replies_count_dto = self._get_comments_replies_count(
            parent_comments_list, comment_replies_count_dict)
        return (post_reactions_dto, post_comments_dto, comments_reactions_dto,
            comment_replies_count_dto)

    @staticmethod
    def _get_user_posts_complete_details_dto(user_posts_details_dto,
        posts_reactions_dto, posts_comments_dto, comments_reactions_dto,
        comment_replies_count_dto):

        post_complete_details_dto = UserPostsCompleteDetailsDto(
            posts_dto=user_posts_details_dto.posts_dto,
            users_dto=user_posts_details_dto.users_dto,
            comments_dto=user_posts_details_dto.comments_dto,
            reactions_dto=user_posts_details_dto.reactions_dto,
            posts_reactions_dto=posts_reactions_dto,
            posts_comments_dto=posts_comments_dto,
            comments_reactions_dto=comments_reactions_dto,
            comment_replies_count_dto=comment_replies_count_dto
        )
        return post_complete_details_dto

    @staticmethod
    def _get_comments_list_dict(comments_dto):

        comments_list_dict = defaultdict(list)
        for comment_dto in comments_dto:
            comments_list_dict['comments'].append(comment_dto.id)
            is_parent_comment = comment_dto.parent_comment_id == None
            if is_parent_comment:
                comments_list_dict['parent_comments'].append(comment_dto.id)
        return comments_list_dict

    @staticmethod
    def _get_comments_replies_count(comment_ids_list,
                                    comment_replies_count_dict):

        return [
            CommentRepliesCountDto(
                comment_id=comment_id,
                replies_count=comment_replies_count_dict.get(comment_id, 0)
            )
            for comment_id in comment_ids_list
        ]

    @staticmethod
    def _get_comment_reactions_dto(comment_ids_list, comments_reactions_dict,
                                   comments_reactions_count_dict):

        comments_reactions_list = [
            CommentReactionsDto(
                comment_id=comment_id,
                reactions_count=comments_reactions_count_dict.get(comment_id, 0),
                reactions=sorted(list(comments_reactions_dict.get(comment_id, [])))
            ) for comment_id in comment_ids_list
        ]
        return comments_reactions_list

    @staticmethod
    def _get_posts_comments_count_dict(posts_comments_count_dict, posts_dto):

        return [
            PostCommentsCountDto(post_id=post_dto.id,
                comments_count=posts_comments_count_dict.get(post_dto.id, 0))
            for post_dto in posts_dto
        ]

    @staticmethod
    def _get_post_reactions_dto(posts_reactions_dict,
            posts_reactions_count_dict, posts_dto):

        post_reactions_list = []
        posts_reactions_dict = dict(sorted(posts_reactions_dict.items()))
        posts_reactions_count_dict = dict(sorted(posts_reactions_count_dict.items()))
        for post in posts_dto:
            post_reactions_list.append(
                PostReactionsDto(post_id=post.id,
                reactions_count=posts_reactions_count_dict.get(post.id, 0),
                reactions=sorted(list(posts_reactions_dict.get(post.id, []))))
            )
        return post_reactions_list

    def _get_reactions_dicts(self, reactions_dto):

        posts_reactions_dict = defaultdict(set)
        posts_reactions_count_dict = defaultdict(int)
        comments_reactions_dict = defaultdict(set)
        comments_reactions_count_dict = defaultdict(int)
        for reaction in reactions_dto:
            if self._is_post_reaction(reaction):
                posts_reactions_count_dict[reaction.post_id] += 1
                posts_reactions_dict[reaction.post_id].add(reaction.reaction)
            else:
                comments_reactions_count_dict[reaction.comment_id] += 1
                comments_reactions_dict[reaction.comment_id].add(
                    reaction.reaction
                )
        return (posts_reactions_dict, posts_reactions_count_dict, comments_reactions_dict,
            comments_reactions_count_dict)

    def _get_comments_dicts(self, comments_dto):

        comment_replies_count_dict = defaultdict(int)
        posts_comments_count_dict = defaultdict(int)
        for comment in comments_dto:
            if comment.parent_comment_id:
                comment_replies_count_dict[comment.parent_comment_id] += 1
            else:
                posts_comments_count_dict[comment.post_id] += 1

        return posts_comments_count_dict, comment_replies_count_dict

    @staticmethod
    def _is_post_reaction(reaction):
        if reaction.post_id:
            return True
        return False
