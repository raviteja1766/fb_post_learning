from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import get_reactions_to_post
from raven.utils import json
from django.http import HttpResponse
from fb_post.exceptions import InvalidPostException
from fb_post.constants import INVALID_POST_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    post_id = kwargs['post_id']

    try:
        reactions_details_list = get_reactions_to_post(post_id=post_id)
    except InvalidPostException:
        raise NotFound(*INVALID_POST_EXCEPTION)

    data = json.dumps(reactions_details_list)
    response = HttpResponse(data, status=200)
    return response