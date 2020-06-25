from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import get_reaction_metrics
from raven.utils import json
from django.http import HttpResponse
from fb_post.exceptions import InvalidPostException
from fb_post.constants import INVALID_POST_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    post_id = kwargs['post_id']
    try:
        reactions_dict = get_reaction_metrics(post_id=post_id)
    except InvalidPostException:
        raise NotFound(*INVALID_POST_EXCEPTION)
    reactions_list = []
    for key, value in reactions_dict.items():
        reactions_list.append({
            "reaction": key,
            "count" : value
        })
    data = json.dumps(reactions_list)
    response = HttpResponse(data, status=200)
    return response