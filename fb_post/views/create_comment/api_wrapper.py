from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import create_comment
from raven.utils import json
from django.http import HttpResponse
from fb_post.exceptions import InvalidPostException
from fb_post.constants import INVALID_POST_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs['user']
    request_data = kwargs['request_data']
    comment_content = request_data['content']
    post_id = kwargs['post_id']
    try:
        comment_id = create_comment(
            user_id=user.id,
            post_id=post_id,
            comment_content=comment_content 
        )
    except InvalidPostException:
        raise NotFound(*INVALID_POST_EXCEPTION)

    data = json.dumps({'comment_id': comment_id})
    response = HttpResponse(data, status=201)
    return response