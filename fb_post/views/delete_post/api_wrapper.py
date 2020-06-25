from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils import delete_post
from django.http import HttpResponse
from fb_post.exceptions import\
    InvalidPostException, UserCannotDeletePostException
from fb_post.constants import\
    INVALID_POST_EXCEPTION, USER_CANNOT_DELETE_POST_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    post_id = kwargs['post_id']

    try:
        delete_post(user_id=user.id, post_id=post_id)
    except InvalidPostException:
        raise NotFound(*INVALID_POST_EXCEPTION)
    except UserCannotDeletePostException:
        raise Forbidden(*USER_CANNOT_DELETE_POST_EXCEPTION)
    response = HttpResponse(status=200)
    return response