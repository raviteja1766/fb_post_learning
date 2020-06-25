from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import get_user_posts
from raven.utils import json
from django.http import HttpResponse

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    query_params = kwargs['request_query_params']
    offset = query_params.offset
    limit = query_params.limit
    total_posts, posts_details_list = get_user_posts(
        user_id=user.id, offset=offset, limit=limit
    )
    user_posts_dict = {
        "total": total_posts,
        "posts": posts_details_list
    }
    data = json.dumps(user_posts_dict)
    response = HttpResponse(data, status=200)
    return response