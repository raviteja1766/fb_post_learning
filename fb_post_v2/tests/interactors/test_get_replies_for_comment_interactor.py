import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.get_replies_for_comment_interactor\
    import GetRepliesForCommentInteractor
from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_v2.interactors.storages.dtos import RepliesForCommentDetailsDto


def test_get_replies_for_comment_given_invalid_details_raises_invalid_comment_id():

    comment_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetRepliesForCommentInteractor(
        storage=storage, presenter=presenter)
    storage.validate_comment_id.return_value = False
    presenter.raise_exception_for_invalid_comment.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_replies_for_comment(comment_id=comment_id)

    # Assert
    storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    presenter.raise_exception_for_invalid_comment.assert_called_once()


def test_get_replies_for_comment_given_valid_details_returns_reply_details(
        replies_users_dtos, replies_dtos, get_replies_for_comment):

    # Arrange
    comment_id = 1
    replies_details_dtos = RepliesForCommentDetailsDto(
        users_dto=replies_users_dtos, replys_dto=replies_dtos
    )
    presenter_response = get_replies_for_comment
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetRepliesForCommentInteractor(
        storage=storage, presenter=presenter)
    storage.validate_comment_id.return_value = True
    storage.get_replies_for_comment_details_dtos\
        .return_value = replies_details_dtos
    presenter.get_response_for_get_replies_for_comment_details_dtos\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_replies_for_comment(comment_id=comment_id)

    # Assert
    storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    storage.get_replies_for_comment_details_dtos\
        .assert_called_once_with(comment_id=comment_id)
    presenter.get_response_for_get_replies_for_comment_details_dtos\
        .assert_called_once_with(replies_details_dtos=replies_details_dtos)
    assert actual_output == presenter_response
