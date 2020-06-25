from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation

from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation
from fb_post_v2.interactors.delete_post_interactor \
    import DeletePostInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    post_id = kwargs['post_id']
    post_storage = PostStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeletePostInteractor(
        storage=post_storage, presenter=presenter
    )

    interactor.delete_post(user_id=user.id, post_id=post_id)

    response = HttpResponse(status=200)
    return response