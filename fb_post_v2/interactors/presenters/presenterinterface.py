from abc import ABC
from abc import abstractmethod
from typing import List, Any, Dict
from fb_post_v2.interactors.storages.dtos import (
    ReactionMetricDto, PostReactionCompleteDetailsDto,
    UserPostsDetailsDto, RepliesForCommentDetailsDto
)
from fb_post_v2.dtos.dtos import (
    PostCompleteDetailsDto, UserPostsCompleteDetailsDto
)

class PresenterInterface(ABC):

    @abstractmethod
    def get_create_post_response(self, post_id: int):
        pass

    @abstractmethod
    def get_create_comment_response(self, comment_id: int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_post(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_comment(self):
        pass

    @abstractmethod
    def get_reply_to_comment_response(self, reply_id: int):
        pass

    @abstractmethod
    def get_total_reaction_count_response(self, count: int):
        pass

    @abstractmethod
    def get_response_for_get_reaction_metrics_of_post(self,
        reaction_metrics_details_dto: List[ReactionMetricDto]):
        pass

    @abstractmethod
    def raise_exception_for_user_cannot_delete_post(self):
        pass

    @abstractmethod
    def get_response_for_get_posts_with_more_positive_reactions(self,
        post_ids_list = List[int]):
        pass

    @abstractmethod
    def get_response_for_get_posts_reacted_by_user(self,
        post_ids_list: List[int]):
        pass

    @abstractmethod
    def get_response_for_get_post_reactions_details_dto(self,
        post_reactions_dtos: PostReactionCompleteDetailsDto):
        pass

    @abstractmethod
    def get_response_for_get_post_details_dto(self,
        post_complete_details_dto: PostCompleteDetailsDto):
        pass

    @abstractmethod
    def get_response_for_get_user_posts_details_dto(self,
        user_posts_complete_details_dto: UserPostsCompleteDetailsDto):
        pass

    @abstractmethod
    def get_response_for_get_replies_for_comment_details_dtos(self,
        replies_details_dtos: RepliesForCommentDetailsDto):
        pass