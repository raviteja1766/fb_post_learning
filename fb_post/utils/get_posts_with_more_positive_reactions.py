from django.db.models import Count, Q, F
from fb_post.models import Post
from fb_post.constants import ReactionType


def get_posts_with_more_positive_reactions():

    positive = Q(reaction__reaction__in=[
        ReactionType.THUMBS_UP.value, ReactionType.LIT.value,
        ReactionType.LOVE.value,ReactionType.HAHA.value,
        ReactionType.WOW.value])

    post_ids = Post.objects.values_list('id', flat=True)\
        .annotate(
            positive_reactions=Count('reaction', filter=positive),
            negative_reactions=Count('reaction', filter=~positive)
        ).filter(positive_reactions__gt=F('negative_reactions'))

    post_ids_list = list(post_ids)

    return post_ids_list
