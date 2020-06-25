from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation
from fb_post_v2.storages.reaction_storage_implementation\
    import ReactionStorageImplementation
from fb_post_v2.interactors.react_to_post_interactor\
    import ReactToPostInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    post_id = kwargs['post_id']
    request_data = kwargs['request_data']
    reaction_type = request_data['reaction_type']
    post_storage = PostStorageImplementation()
    reaction_storage = ReactionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = ReactToPostInteractor(
        presenter=presenter, post_storage=post_storage,
        reaction_storage=reaction_storage
    )

    interactor_response = interactor.react_to_post(
        user_id=user.id, post_id=post_id, reaction_type=reaction_type
    )

    response = HttpResponse(status=201)
    return response
