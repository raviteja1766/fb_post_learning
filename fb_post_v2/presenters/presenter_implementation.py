from typing import List, Any, Dict
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from fb_post_v2.constants.exception_messages import *
from fb_post_v2.dtos.dtos import *
from fb_post_v2.interactors.storages.dtos import *
from collections import defaultdict

class PresenterImplementation(PresenterInterface):

    def get_create_post_response(self, post_id: int):

        return {"post_id": post_id}

    def get_create_comment_response(self, comment_id: int):

        return {"comment_id": comment_id}

    def get_reply_to_comment_response(self, reply_id: int):

        return {"reply_id": reply_id}

    def raise_exception_for_invalid_post(self):

        raise NotFound(*INVALID_POST_EXCEPTION)

    def raise_exception_for_invalid_comment(self):

        raise NotFound(*INVALID_COMMENT_EXCEPTION)

    def get_total_reaction_count_response(self, count: int):
        pass

    def get_response_for_get_reaction_metrics_of_post(self,
            reaction_metrics_details_dto: List[ReactionMetricDto]):
        pass

    def raise_exception_for_user_cannot_delete_post(self):
        
        raise Forbidden(*USER_CANNOT_DELETE_POST_EXCEPTION)

    def get_response_for_get_posts_with_more_positive_reactions(self,
            post_ids_list = List[int]):
        pass


    def get_response_for_get_posts_reacted_by_user(self,
            post_ids_list: List[int]):
        pass


    def get_response_for_get_post_reactions_details_dto(self,
            post_reactions_dtos: PostReactionCompleteDetailsDto):
        pass

    def get_response_for_get_user_posts_details_dto(self,
            user_posts_complete_details_dto: UserPostsCompleteDetailsDto):

        posts_dto = user_posts_complete_details_dto.posts_dto
        users_dto = user_posts_complete_details_dto.users_dto
        users_dto_dict = self._get_users_dto_dict(users_dto)
        comments_dto = user_posts_complete_details_dto.comments_dto
        comments_dict = self._get_posts_comments_dict(comments_dto)
        posts_reactions_dto = \
            user_posts_complete_details_dto.posts_reactions_dto
        posts_reactions_dict = \
            self._get_posts_reactions_dict(posts_reactions_dto)
        posts_comments_count_dto = \
            user_posts_complete_details_dto.posts_comments_dto
        posts_comments_count_dict = \
            self._get_posts_comments_count_dict(posts_comments_count_dto)
        comments_reactions_dto = \
            user_posts_complete_details_dto.comments_reactions_dto
        comment_replies_count_dto = \
            user_posts_complete_details_dto.comment_replies_count_dto
        return self._get_user_posts_details(
            posts_dto, users_dto_dict, comments_dict, posts_reactions_dict,
            posts_comments_count_dict, comments_reactions_dto,
            comment_replies_count_dto
        )

    def _get_user_posts_details(
            self, posts_dto, users_dto_dict, comments_dict,
            posts_reactions_dict, posts_comments_count_dict,
            comments_reactions_dto, comment_replies_count_dto
            ):

        return [
            self._get_post_details(post_dto, users_dto_dict, comments_dict,
            posts_reactions_dict, posts_comments_count_dict,
            comments_reactions_dto, comment_replies_count_dto)
            for post_dto in posts_dto
        ]

    def _get_post_details(self, post_dto, users_dto_dict, comments_dict,
            posts_reactions_dict, posts_comments_count_dict,
            comments_reactions_dto, comment_replies_count_dto):

        comments_dto = comments_dict[post_dto.id]
        post_reactions_dto = posts_reactions_dict[post_dto.id]
        post_comments_dto = posts_comments_count_dict[post_dto.id]

        return {
            "post_id": post_dto.id,
            "posted_by": self._convert_user_dto_to_dict(
                users_dto_dict[post_dto.posted_by_id]
            ),
            "posted_at": self._convert_datetime_obj_to_string(
                post_dto.posted_at),
            "post_content": post_dto.post_content,
            "reactions": {
                "count": post_reactions_dto.reactions_count,
                "type": post_reactions_dto.reactions
            },
            "comments": self._get_comments_dict(
                users_dto_dict, comments_dto, comments_reactions_dto,
                comment_replies_count_dto
            ),
            "comments_count": post_comments_dto.comments_count,
        }

    @staticmethod
    def _get_posts_comments_count_dict(posts_comments_count_dto):

        comments_count_dict = {}
        for comment_count in posts_comments_count_dto:
            comments_count_dict[comment_count.post_id] = comment_count
        return comments_count_dict

    @staticmethod
    def _get_posts_reactions_dict(posts_reactions_dto):

        posts_reactions_dict = {}
        for post_reaction in posts_reactions_dto:
            posts_reactions_dict[post_reaction.post_id] = post_reaction
        return posts_reactions_dict

    def _get_posts_comments_dict(self, comments_dto):

        comments_dict_dto = defaultdict(list)
        for comment in comments_dto:
            comments_dict_dto[comment.post_id].append(comment)
        return comments_dict_dto

    def get_response_for_get_post_details_dto(self,
            post_complete_details_dto: PostCompleteDetailsDto):

        post_dto = post_complete_details_dto.post_dto
        comments_dto = post_complete_details_dto.comments_dto
        users_dto = post_complete_details_dto.users_dto
        users_dto_dict = self._get_users_dto_dict(users_dto)
        post_reactions_dto = post_complete_details_dto.post_reactions_dto
        post_comments_dto = post_complete_details_dto.post_comments_dto
        comments_reactions_dto = post_complete_details_dto\
            .comments_reactions_dto
        comment_replies_count_dto = post_complete_details_dto\
            .comment_replies_count_dto

        return {
            "post_id": post_dto.id,
            "posted_by": self._convert_user_dto_to_dict(
                users_dto_dict[post_dto.posted_by_id]
            ),
            "posted_at": self._convert_datetime_obj_to_string(
                post_dto.posted_at),
            "post_content": post_dto.post_content,
            "reactions": {
                "count": post_reactions_dto.reactions_count,
                "type": post_reactions_dto.reactions
            },
            "comments": self._get_comments_dict(
                users_dto_dict, comments_dto, comments_reactions_dto,
                comment_replies_count_dto
            ),
            "comments_count": post_comments_dto.comments_count,
        }

    def _get_comments_dict(self, users_dto_dict, comments_dto,
                           comments_reactions_dto,
                           comment_replies_count_dto):


        parent_comments_list, parent_comments_dict =\
            self.get_parent_comments_replies_dict(comments_dto)
        comments_reactions_dto_dict = self.get_comments_reactions_dto_dict(
            comments_reactions_dto)
        comment_replies_count_dto = self.get_comment_replies_count_dto_dict(
            comment_replies_count_dto)

        return [
            self._convert_post_comment_dto_to_dict(
                comment_dto, parent_comments_dict[comment_dto.id],
                comments_reactions_dto_dict, users_dto_dict,
                comment_replies_count_dto[comment_dto.id]
            )
            for comment_dto in parent_comments_list
        ]


    def _convert_post_comment_dto_to_dict(self, comment_dto, replies_dto,
        comments_reactions_dto_dict, users_dto_dict, comment_replies_count_dto):

        user_dto = users_dto_dict[comment_dto.commented_by_id]
        comment_dict = self._convert_comment_dto_to_dict(comment_dto, user_dto)
        comment_extra_dict = {
            "reactions": self.get_reaction_details_to_comment(
                comments_reactions_dto_dict[comment_dto.id]
            ),
            "replies_count": comment_replies_count_dto.replies_count,
            "replies": self.get_replies_details_dict(
                replies_dto, comments_reactions_dto_dict, users_dto_dict
            )
        }
        comment_dict.update(comment_extra_dict)
        return comment_dict


    def get_replies_details_dict(self, replies_dto,
                                 comments_reactions_dto_dict,
                                 users_dto_dict):

        return [
            self.get_reply_dto_to_dict(
                reply_dto,comments_reactions_dto_dict[reply_dto.id],
                users_dto_dict[reply_dto.commented_by_id]
            )
            for reply_dto in replies_dto
        ]

    def get_reply_dto_to_dict(self, reply_dto, comment_reactions_dto,
                              user_dto):

        reply_dict = self._convert_comment_dto_to_dict(reply_dto, user_dto)
        reply_dict["reactions"] = self.get_reaction_details_to_comment(
            comment_reactions_dto
        )
        return reply_dict

    @staticmethod
    def get_reaction_details_to_comment(comments_reactions_dto):

        return {
            "type": comments_reactions_dto.reactions,
            "count": comments_reactions_dto.reactions_count
        }

    @staticmethod
    def get_comment_replies_count_dto_dict(comment_replies_count_dto):

        comment_replies_count_dto_dict = {}
        for comment_dto in comment_replies_count_dto:
            comment_replies_count_dto_dict[comment_dto.comment_id] =\
                comment_dto
        return comment_replies_count_dto_dict

    @staticmethod
    def get_comments_reactions_dto_dict(comments_reactions_dto):

        comments_reactions_dto_dict = {}
        for comment_dto in comments_reactions_dto:
            comments_reactions_dto_dict[comment_dto.comment_id] =\
                comment_dto
        return comments_reactions_dto_dict



    def get_parent_comments_replies_dict(self, comments_dto):

        parent_comments_dict = defaultdict(list)
        parent_comments_list = []
        for comment_dto in comments_dto:
            if self._check_for_parent_comment(comment_dto):
                parent_comments_list.append(comment_dto)
            else:
                parent_comments_dict[comment_dto.parent_comment_id].append(
                    comment_dto)
        return parent_comments_list, parent_comments_dict


    @staticmethod
    def _check_for_parent_comment(comment_dto):
        is_reply = comment_dto.parent_comment_id
        is_parent_comment = not is_reply
        return is_parent_comment


    @staticmethod
    def _get_users_dto_dict(users_dto):

        users_dto_dict = {}
        for user_dto in users_dto:
            users_dto_dict[user_dto.id] = user_dto
        return users_dto_dict


    def get_response_for_get_replies_for_comment_details_dtos(self,
        replies_details_dtos: RepliesForCommentDetailsDto):

        users_dto = replies_details_dtos.users_dto
        replys_dto = replies_details_dtos.replys_dto

        users_dto_dict = {}
        for user_dto in users_dto:
            users_dto_dict[user_dto.id] = user_dto

        replys_dict = self.get_replies_dict_details(
            replys_dto, users_dto_dict
        )
        return replys_dict

    def get_replies_dict_details(self, replys_dto, users_dto_dict):

        replys_dict = [
            self._convert_comment_dto_to_dict(
                reply_dto, users_dto_dict[reply_dto.commented_by_id]
            ) for reply_dto in replys_dto
        ]

        return replys_dict


    def _convert_comment_dto_to_dict(self, reply_dto, user_dto):
        return {
            "comment_id": reply_dto.id,
            "commenter": self._convert_user_dto_to_dict(user_dto),
            "commented_at": self._convert_datetime_obj_to_string(
                reply_dto.commented_at
            ),
            "comment_content": reply_dto.comment_content
        }

    @staticmethod
    def _convert_user_dto_to_dict(user_dto):

        return {
            "user_id": user_dto.id,
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic
        }

    @staticmethod
    def _convert_datetime_obj_to_string(datetime_obj):

        return datetime_obj.strftime("%m-%d-%Y %X.%f")
