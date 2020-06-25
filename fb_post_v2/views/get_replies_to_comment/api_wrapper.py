from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation

from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation
from fb_post_v2.interactors.get_replies_for_comment_interactor\
    import GetRepliesForCommentInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    comment_id = kwargs['comment_id']
    storage = CommentStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetRepliesForCommentInteractor(
        storage=storage, presenter=presenter
    )

    interactor_response = interactor.get_replies_for_comment(
        comment_id=comment_id)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response