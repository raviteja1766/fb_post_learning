from fb_post.models import Comment
from .validations import is_valid_comment
from .get_post import get_comment_details


def get_replies_for_comment(comment_id):

    is_valid_comment(comment_id)
    comment_objs = Comment.objects\
        .filter(parent_comment_id=comment_id)\
        .select_related('commented_by')

    replies_list = [get_comment_details(comment) for comment in comment_objs]

    return replies_list
