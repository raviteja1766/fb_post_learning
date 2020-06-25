from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation

from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation
from fb_post_v2.interactors.get_post_interactor import GetPostInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    post_id = kwargs["post_id"]
    post_storage = PostStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetPostInteractor(
        storage=post_storage, presenter=presenter
    )

    interactor_response = interactor.get_post(post_id=post_id)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response