from abc import ABC, abstractmethod
from fb_post_v2.constants.enums import ReactionType
from typing import List
from fb_post_v2.interactors.storages.dtos import (
    RepliesForCommentDetailsDto
)


class CommentStorageInterface(ABC):
    
    @abstractmethod
    def validate_comment_id(self, comment_id: int):
        pass
    
    @abstractmethod
    def create_comment(self, user_id: int, post_id: int,
                       comment_content: str) -> int:
        pass
    
    @abstractmethod
    def get_parent_comment_id(self, comment_id: int):
        pass

    @abstractmethod
    def reply_to_comment(self, user_id: int, comment_id: int,
                         reply_content: str) -> int:
        pass
    
    @abstractmethod
    def get_replies_for_comment_details_dtos(self,
        comment_id: int) -> RepliesForCommentDetailsDto:
        pass