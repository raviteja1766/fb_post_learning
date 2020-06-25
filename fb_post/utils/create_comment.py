from fb_post.models.comment import Comment
from .validations import (
    is_valid_user,
    is_valid_post,
    is_valid_comment_content
)


def create_comment(user_id, post_id, comment_content):

    is_valid_user(user_id)
    is_valid_post(post_id)
    is_valid_comment_content(comment_content)

    comment_obj = Comment.objects.create(
        content=comment_content,
        commented_by_id=user_id,
        post_id=post_id
    )
    return comment_obj.id
