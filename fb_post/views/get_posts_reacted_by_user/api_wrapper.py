from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import get_posts_reacted_by_user
from raven.utils import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    post_ids_list = get_posts_reacted_by_user(user_id=user.id)

    data = json.dumps(post_ids_list)
    response = HttpResponse(data, status=200)
    return response