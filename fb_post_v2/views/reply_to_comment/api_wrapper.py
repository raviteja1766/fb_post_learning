from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation

from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation
from fb_post_v2.interactors.reply_to_comment_interactor\
    import ReplyToCommentInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs['request_data']
    comment_id = kwargs['comment_id']
    reply_content = request_data['content']
    storage = CommentStorageImplementation()
    presenter = PresenterImplementation()
    interactor = ReplyToCommentInteractor(
        storage=storage, presenter=presenter
    )

    interactor_response = interactor.reply_to_comment(
        user_id=user.id,comment_id=comment_id, reply_content=reply_content
    )

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response