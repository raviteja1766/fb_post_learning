from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import get_replies_for_comment
from raven.utils import json
from django.http import HttpResponse
from fb_post.exceptions import InvalidCommentException
from fb_post.constants import INVALID_COMMENT_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    comment_id = kwargs['comment_id']

    try:
        reply_details = get_replies_for_comment(comment_id=comment_id)
    except InvalidCommentException:
        raise NotFound(*INVALID_COMMENT_EXCEPTION)

    data = json.dumps(reply_details)
    response = HttpResponse(data, status=200)
    return response