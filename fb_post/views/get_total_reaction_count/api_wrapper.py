from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import get_total_reaction_count
from raven.utils import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    reactions_count = get_total_reaction_count()
    data = json.dumps(reactions_count)
    response = HttpResponse(data, status=200)
    return response