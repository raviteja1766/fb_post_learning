import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.reply_to_comment_interactor\
    import ReplyToCommentInteractor
from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound


def test_reply_to_comment_given_valid_details_returns_reply_id():

    # Arrange
    user_id = 1
    comment_id = 1
    reply_id = 2
    reply_content = "hey how are you man..?"
    presenter_response = {
        "reply_id": reply_id
    }
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReplyToCommentInteractor(storage=storage, presenter=presenter)
    storage.reply_to_comment.return_value = reply_id
    storage.validate_comment_id.return_value = True
    storage.get_parent_comment_id.return_value = None
    presenter.get_reply_to_comment_response.return_value = presenter_response

    # Act
    interactor_response = interactor.reply_to_comment(
        user_id=user_id, comment_id=comment_id, reply_content=reply_content
    )

    # Assert
    storage.reply_to_comment.assert_called_once_with(
        user_id=user_id, comment_id=comment_id, reply_content=reply_content
    )
    presenter.get_reply_to_comment_response\
        .assert_called_once_with(reply_id = reply_id)
    storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    storage.get_parent_comment_id\
        .assert_called_once_with(comment_id=comment_id)
    assert interactor_response['reply_id'] == presenter_response['reply_id']


def test_reply_to_comment_given_valid_details_with_reply_id_returns_reply_id():

    # Arrange
    user_id = 1
    parent_comment_id = 1
    comment_id = 2
    reply_id = 3
    reply_content = "hey how do you do..?"
    presenter_response = {
        "reply_id": reply_id
    }
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReplyToCommentInteractor(storage=storage,presenter=presenter)
    storage.reply_to_comment.return_value = reply_id
    storage.validate_comment_id.return_value = True
    storage.get_parent_comment_id.return_value = parent_comment_id
    presenter.get_reply_to_comment_response.return_value = presenter_response

    # Act
    interactor_response = interactor.reply_to_comment(
        user_id=user_id, comment_id=comment_id, reply_content=reply_content
    )

    # Assert
    storage.reply_to_comment.assert_called_once_with(
        user_id=user_id, comment_id=parent_comment_id,
        reply_content=reply_content
    )
    presenter.get_reply_to_comment_response\
        .assert_called_once_with(reply_id = reply_id)
    storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    storage.get_parent_comment_id\
        .assert_called_once_with(comment_id=comment_id)
    assert interactor_response['reply_id'] == presenter_response['reply_id']

def test_reply_to_comment_given_invalid_details_raises_invalid_comment_id():

    user_id = 1
    comment_id = 1
    reply_content = "hey how are you man..?"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReplyToCommentInteractor(storage=storage,
                                          presenter=presenter)
    storage.validate_comment_id.return_value = False
    presenter.raise_exception_for_invalid_comment.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.reply_to_comment(
            user_id=user_id, comment_id=comment_id,
            reply_content=reply_content
        )

    # Assert
    storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    presenter.raise_exception_for_invalid_comment.assert_called_once()
