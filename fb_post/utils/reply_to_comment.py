from fb_post.models import Comment
from .validations import (
    is_valid_user, is_valid_comment,
    is_valid_reply_comment_content
)


def reply_to_comment(user_id, comment_id, reply_content):

    is_valid_user(user_id)
    comment = is_valid_comment(comment_id)
    is_valid_reply_comment_content(reply_content)

    is_not_comment = comment.parent_comment_id

    if is_not_comment:
        comment_id = comment.parent_comment_id

    reply_obj = Comment.objects.create(
        content=reply_content,
        commented_by_id=user_id,
        post_id=comment.post_id,
        parent_comment_id=comment_id
    )
    return reply_obj.id
