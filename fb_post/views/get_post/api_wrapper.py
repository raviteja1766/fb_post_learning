from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import get_post
from raven.utils import json
from django.http import HttpResponse
from fb_post.exceptions import InvalidPostException
from fb_post.constants import INVALID_POST_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post.dto import Post


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    post_id = kwargs['post_id']

    try:
        post_dict = get_post(post_id=post_id)
    except InvalidPostException:
        raise NotFound(*INVALID_POST_EXCEPTION)

    data = Post(**post_dict)
    json_data = json.dumps(data)
    response = HttpResponse(json_data, status=200)
    return response