from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import react_to_post
from django.http import HttpResponse
from fb_post.exceptions import InvalidPostException
from fb_post.constants import INVALID_POST_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs['request_data']
    post_id = kwargs['post_id']
    reaction_type = request_data['reaction_type']

    try:
        react_to_post(
            user_id=user.id,
            post_id=post_id,
            reaction_type=reaction_type
        )
    except InvalidPostException:
        raise NotFound(*INVALID_POST_EXCEPTION)

    response = HttpResponse(status=200)
    return response