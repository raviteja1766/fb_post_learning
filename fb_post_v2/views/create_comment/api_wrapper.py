from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation

from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation
from fb_post_v2.interactors.create_comment_interactor import CreateCommentInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs['request_data']
    comment_content = request_data['content']
    post_id = kwargs['post_id']
    comment_storage = CommentStorageImplementation()
    post_storage = PostStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateCommentInteractor(
        post_storage=post_storage, presenter=presenter,
        comment_storage=comment_storage
    )

    interactor_response = interactor.create_comment(
        user_id=user.id, post_id=post_id, comment_content=comment_content)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response