from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import create_post
from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs['request_data']
    post_content = request_data['content']

    post_id = create_post(user_id=user.id, post_content=post_content)

    data = json.dumps({'post_id': post_id})
    response = HttpResponse(data, status=201)
    return response