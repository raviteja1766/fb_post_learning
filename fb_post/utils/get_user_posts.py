from django.db.models import Prefetch
from fb_post.models import Comment, Post
from .get_post import get_post_details
from .validations import is_valid_user


def get_user_posts(user_id,offset,limit):

    is_valid_user(user_id)
    queryset = Comment.objects\
        .select_related('commented_by')\
        .prefetch_related('reaction_set')
    post_objs = Post.objects\
        .filter(posted_by_id=user_id)\
        .select_related('posted_by')\
        .prefetch_related(
            'reaction_set',
            Prefetch('comment_set', queryset=queryset, to_attr='comments')
        )
    total_posts = len(post_objs)
    post_objs = post_objs[offset: offset + limit]
    posts_details_list = [get_post_details(post) for post in post_objs]

    return total_posts,posts_details_list
