import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.create_comment_interactor\
    import CreateCommentInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound



def test_create_comment_given_valid_details_returns_comment_id():

    # Arrange
    user_id = 1
    post_id = 1
    comment_id = 1
    comment_content = "hii there..."
    presenter_response = {
        "comment_id": comment_id
    }
    post_storage = create_autospec(PostStorageInterface)
    comment_storage = create_autospec(CommentStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCommentInteractor(post_storage=post_storage,
        comment_storage=comment_storage, presenter=presenter)
    post_storage.validate_post_id.return_value = True
    comment_storage.create_comment.return_value = comment_id
    presenter.get_create_comment_response.return_value = presenter_response

    # Act
    interactor_response = interactor.create_comment(
        user_id=user_id, post_id=post_id, comment_content=comment_content
    )

    # Assert
    comment_storage.create_comment.assert_called_once_with(
        user_id=user_id, post_id=post_id, comment_content=comment_content
    )
    presenter.get_create_comment_response.assert_called_once_with(
        comment_id = comment_id
    )
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    assert interactor_response['comment_id'] ==\
        presenter_response['comment_id']


def test_create_comment_given_invalid_details_raises_invalid_post_id():

    # Arrange
    user_id = 1
    post_id = 1
    comment_content = "hii there..."

    post_storage = create_autospec(PostStorageInterface)
    comment_storage = create_autospec(CommentStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCommentInteractor(post_storage=post_storage,
        comment_storage=comment_storage, presenter=presenter)
    post_storage.validate_post_id.return_value = False
    presenter.raise_exception_for_invalid_post.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_comment(
            user_id=user_id, post_id=post_id,
            comment_content=comment_content
        )

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    presenter.raise_exception_for_invalid_post.assert_called_once()