from dataclasses import dataclass
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
    CommentDto, ReactionDto, PostDto, PostDetailsDto,
    UserPostsDetailsDto
)
from typing import List

@dataclass()
class PostReactionsDto:
    post_id: int
    reactions: List[ReactionType]
    reactions_count: int

@dataclass()
class PostCommentsCountDto:
    post_id: int
    comments_count: int

@dataclass()
class CommentReactionsDto:
    comment_id: int
    reactions: List[ReactionType]
    reactions_count: int


@dataclass()
class CommentRepliesCountDto:
    comment_id: int
    replies_count: int

@dataclass()
class PostCompleteDetailsDto(PostDetailsDto):
    post_reactions_dto: PostReactionsDto
    post_comments_dto: PostCommentsCountDto
    comments_reactions_dto: List[CommentReactionsDto]
    comment_replies_count_dto: List[CommentRepliesCountDto]

@dataclass()
class UserPostsCompleteDetailsDto(UserPostsDetailsDto):
    posts_reactions_dto: List[PostReactionsDto]
    posts_comments_dto: List[PostCommentsCountDto]
    comments_reactions_dto: List[CommentReactionsDto]
    comment_replies_count_dto: List[CommentRepliesCountDto]
    