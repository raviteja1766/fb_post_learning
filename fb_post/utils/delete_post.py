from fb_post.exceptions import UserCannotDeletePostException
from .validations import is_valid_user, is_valid_post


def delete_post(user_id, post_id):

    is_valid_user(user_id)
    post_obj = is_valid_post(post_id)
    is_post_posted_by_user = post_obj.posted_by_id == user_id

    if is_post_posted_by_user:
        post_obj.delete()
    else:
        raise UserCannotDeletePostException
