from datetime import datetime
from dataclasses import dataclass
from fb_post_v2.constants.enums import ReactionType
from typing import List, Optional


@dataclass()
class ReactionMetricDto:
    reaction_type: ReactionType
    reaction_count: int


@dataclass()
class UserDto:
    id: int
    name: str
    profile_pic: str


@dataclass()
class CommentDto:
    id: int
    commented_by_id: int
    post_id: Optional[int]
    comment_content: str
    commented_at: datetime
    parent_comment_id: Optional


@dataclass()
class ReactionDto:
    id: int
    comment_id: Optional[int]
    post_id: Optional[int]
    reacted_by_id: int
    reaction: ReactionType


@dataclass()
class PostDto:
    id: int
    post_content: str
    posted_by_id: int
    posted_at: datetime


@dataclass()
class PostDetailsDto:
    post_dto: PostDto
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]

@dataclass()
class UserPostsDetailsDto:
    posts_dto: List[PostDto]
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]

@dataclass()
class PostReactionCompleteDetailsDto:
    user_dtos: List[UserDto]
    reaction_dtos: List[ReactionDto]

@dataclass()
class RepliesForCommentDetailsDto:
    users_dto: List[UserDto]
    replys_dto: List[CommentDto]


