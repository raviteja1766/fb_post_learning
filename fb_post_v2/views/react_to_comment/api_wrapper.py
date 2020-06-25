from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation
from fb_post_v2.storages.reaction_storage_implementation\
    import ReactionStorageImplementation
from fb_post_v2.interactors.react_to_comment_interactor\
    import ReactToCommentInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    comment_id = kwargs['comment_id']
    request_data = kwargs['request_data']
    reaction_type = request_data['reaction_type']
    comment_storage = CommentStorageImplementation()
    reaction_storage = ReactionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = ReactToCommentInteractor(
        presenter=presenter, comment_storage=comment_storage,
        reaction_storage=reaction_storage
    )

    interactor_response = interactor.react_to_comment(
        user_id=user.id, comment_id=comment_id, reaction_type=reaction_type
    )

    response = HttpResponse(status=201)
    return response
