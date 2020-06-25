from fb_post.models import (
    User, Post, Comment)
from fb_post.exceptions import (
    InvalidUserException, InvalidCommentException, InvalidCommentContent,
    InvalidPostContent, InvalidPostException, InvalidReplyContent,
    InvalidReactionTypeException)
from fb_post.constants import ReactionType


def is_valid_user(user_id):

    try:
        user_obj = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise InvalidUserException
    return user_obj


def is_valid_post(post_id):

    try:
        post_obj = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException
    return post_obj


def is_valid_comment(comment_id):

    try:
        comment_obj = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        raise InvalidCommentException
    return comment_obj


def is_valid_post_content(post_content):

    is_post_content_empty = not post_content

    if is_post_content_empty:
        raise InvalidPostContent


def is_valid_comment_content(comment_content):

    is_comment_content_empty = not comment_content

    if is_comment_content_empty:
        raise InvalidCommentContent


def is_valid_reply_comment_content(reply_content):

    is_reply_content_empty = not reply_content

    if is_reply_content_empty:
        raise InvalidReplyContent


def is_valid_reaction_type(reaction_type):

    is_not_reaction_type = reaction_type not in [
        reaction.value for reaction in ReactionType
    ]

    if is_not_reaction_type:
        raise InvalidReactionTypeException
