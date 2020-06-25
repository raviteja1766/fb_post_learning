from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import reply_to_comment
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
    reply_content = request_data['content']

    try:
        reply_id = reply_to_comment(
            user_id=user.id,
            comment_id=comment_id,
            reply_content=reply_content
        )
    except InvalidCommentException:
        raise NotFound(*INVALID_COMMENT_EXCEPTION)

    data = json.dumps({'reply_id': reply_id})
    response = HttpResponse(data, status=201)
    return response
