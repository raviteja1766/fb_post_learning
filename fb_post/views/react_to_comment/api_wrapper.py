from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import react_to_comment
from raven.utils import json
from django.http import HttpResponse
from fb_post.exceptions import InvalidCommentException
from fb_post.constants import INVALID_COMMENT_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs['request_data']
    comment_id = kwargs['comment_id']
    reaction_type = request_data['reaction_type']

    try:
        react_to_comment(
            user_id=user.id,
            comment_id=comment_id,
            reaction_type=reaction_type
        )
    except InvalidCommentException:
        raise NotFound(*INVALID_COMMENT_EXCEPTION)

    response = HttpResponse(status=200)
    return response