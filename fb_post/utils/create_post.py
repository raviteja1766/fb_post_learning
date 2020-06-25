from fb_post.models import Post
from .validations import is_valid_post_content, is_valid_user


def create_post(user_id, post_content):

    is_valid_user(user_id)
    is_valid_post_content(post_content)

    post_obj = Post.objects.create(
        content=post_content,
        posted_by_id=user_id
    )
    return post_obj.id
