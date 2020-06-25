from abc import ABC, abstractmethod
from typing import List
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
    ReactionMetricDto, PostReactionCompleteDetailsDto
)


class ReactionStorageInterface(ABC):
    
    @abstractmethod
    def get_post_reactions_details_dto(self,
        post_id: int) -> PostReactionCompleteDetailsDto:
        pass
    
    @abstractmethod
    def get_total_reaction_count(self) -> int:
        pass

    @abstractmethod
    def get_reaction_metrics_of_post_dto(self,
        post_id: int) -> List[ReactionMetricDto]:
        pass
    
    @abstractmethod
    def get_old_post_reaction_if_exists(self,
        user_id: int, post_id:int) -> ReactionType:
        pass

    @abstractmethod
    def react_to_post(self, user_id: int, post_id: int,
        reaction_type: ReactionType):
        pass

    @abstractmethod
    def undo_post_reaction(self, user_id: int, post_id: int):
        pass

    @abstractmethod
    def update_post_reaction(self, user_id: int, post_id: int,
        reaction_type: ReactionType):
        pass
    
    @abstractmethod
    def get_old_comment_reaction_if_exists(self,
        user_id: int, comment_id:int) -> ReactionType:
        pass
    
    @abstractmethod
    def react_to_comment(self, user_id: int, comment_id: int,
        reaction_type: ReactionType):
        pass

    @abstractmethod
    def undo_comment_reaction(self, user_id: int, comment_id: int):
        pass

    @abstractmethod
    def update_comment_reaction(self, user_id: int, comment_id: int,
        reaction_type: ReactionType):
        pass