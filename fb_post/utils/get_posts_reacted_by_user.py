from fb_post.models import Post, Reaction
from .validations import is_valid_user


def get_posts_reacted_by_user(user_id):

    is_valid_user(user_id)

    post_ids_list = Post.objects\
        .values_list('id', flat=True)\
        .filter(reaction__in=Reaction.objects.filter(reacted_by_id=user_id))\
        .distinct()

    return list(post_ids_list)
