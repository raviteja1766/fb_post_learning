from abc import ABC, abstractmethod
from fb_post_v2.constants.enums import ReactionType
from typing import List
from fb_post_v2.interactors.storages.dtos import (
    PostReactionCompleteDetailsDto, PostDetailsDto,
    UserPostsDetailsDto
)


class PostStorageInterface(ABC):
    
    @abstractmethod
    def validate_post_id(self, post_id: int):
        pass
    
    @abstractmethod
    def create_post(self, user_id: int, post_content: str) -> int:
        pass
    
    @abstractmethod
    def delete_post(self,post_id: int):
        pass

    @abstractmethod
    def get_user_of_post(self, post_id: int) -> int:
        pass

    @abstractmethod
    def get_posts_with_more_positive_reactions(self) -> List[int]:
        pass

    @abstractmethod
    def get_posts_reacted_by_user(self, user_id: int) -> List[int]:
        pass
    
    @abstractmethod
    def get_post_details_dto(self, post_id: int) -> PostDetailsDto:
        pass

    @abstractmethod
    def get_user_posts_details_dto(self,
        user_id: int) -> UserPostsDetailsDto:
        pass
    