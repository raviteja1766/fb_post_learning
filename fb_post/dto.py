from typing import *
from dataclasses import dataclass


@dataclass
class User:
    name: str
    user_id: int
    profile_pic: str

@dataclass
class Reaction:
    count: int
    type: str

@dataclass
class Reply:
    comment_id: int
    commenter: User
    commented_at: str
    comment_content: str
    reactions: Reaction

    def __post_init__(self):
        self.commenter = User(**(self.commenter))
        self.reactions = Reaction(**self.reactions)

@dataclass
class Comment:
    comment_id: int
    commenter: User
    commented_at: str
    comment_content: str
    reactions: Reaction
    replies_count: int
    replies: List[Reply]

    def __post_init__(self):
        self.commenter = User(**(self.commenter))
        self.reactions = Reaction(**self.reactions)
        self.replies = [Reply(**data) for data in self.replies]

@dataclass
class Post:
    post_id: int
    posted_by: Dict[str, Any]
    posted_at: str
    post_content: str
    reactions : Dict[str, Any]
    comments: List[Dict[str, Any]]
    comments_count: int

    def __post_init__(self):
        self.posted_by = User(**(self.posted_by))
        self.comments = [Comment(**data) for data in self.comments]
        self.reactions = Reaction(**self.reactions)
