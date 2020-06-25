import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.get_post_interactor\
    import GetPostInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound


def test_get_post_given_invalid_details_raises_invalid_post_id():

    # Arrange
    post_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = False
    presenter.raise_exception_for_invalid_post.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_post(post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    presenter.raise_exception_for_invalid_post.assert_called_once()


def test_get_post_given_valid_details_returns_post_details(
        post_details_dto, post_complete_details_dto, get_post_response):

    # Arrange
    presenter_response = get_post_response
    post_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = True
    storage.get_post_details_dto.return_value = post_details_dto
    presenter.get_response_for_get_post_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_post(post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    storage.get_post_details_dto.assert_called_once_with(post_id=post_id)
    presenter.get_response_for_get_post_details_dto\
        .assert_called_once_with(post_complete_details_dto=post_complete_details_dto)
    assert actual_output == presenter_response


def test_get_post_when_zero_comments_returns_post_details(
        post_empty_comments_details_dto, post_empty_comments_complete_details_dto,
        get_post_response):

    # Arrange
    presenter_response = get_post_response
    post_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = True
    storage.get_post_details_dto.return_value = post_empty_comments_details_dto
    presenter.get_response_for_get_post_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_post(post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    storage.get_post_details_dto.assert_called_once_with(post_id=post_id)
    presenter.get_response_for_get_post_details_dto\
        .assert_called_once_with(
            post_complete_details_dto=post_empty_comments_complete_details_dto)
    assert actual_output == presenter_response


def test_get_post_when_zero_post_reactions_returns_post_details(
        post_empty_reactions_details_dto,
        post_empty_reactions_complete_details_dto,
        get_post_response):

    # Arrange
    presenter_response = get_post_response
    post_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = True
    storage.get_post_details_dto.return_value = post_empty_reactions_details_dto
    presenter.get_response_for_get_post_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_post(post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    storage.get_post_details_dto.assert_called_once_with(post_id=post_id)
    presenter.get_response_for_get_post_details_dto\
        .assert_called_once_with(
            post_complete_details_dto=post_empty_reactions_complete_details_dto)
    assert actual_output == presenter_response


def test_get_post_when_zero_parent_comment_reactions_returns_post_details(
        post_comment_empty_reactions_details_dto,
        post_comment_empty_reactions_complete_details_dto,
        get_post_response):

    # Arrange
    presenter_response = get_post_response
    post_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = True
    storage.get_post_details_dto.return_value =\
        post_comment_empty_reactions_details_dto
    presenter.get_response_for_get_post_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_post(post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    storage.get_post_details_dto.assert_called_once_with(post_id=post_id)
    presenter.get_response_for_get_post_details_dto\
        .assert_called_once_with(post_complete_details_dto=\
        post_comment_empty_reactions_complete_details_dto)
    assert actual_output == presenter_response
    

def test_get_post_with_zero_replies_returns_post_details(
        post_empty_replies_details_dto,
        post_empty_replies_complete_details_dto,
        get_post_response):

    # Arrange
    presenter_response = get_post_response
    post_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = True
    storage.get_post_details_dto.return_value =\
        post_empty_replies_details_dto
    presenter.get_response_for_get_post_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_post(post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    storage.get_post_details_dto.assert_called_once_with(post_id=post_id)
    presenter.get_response_for_get_post_details_dto\
        .assert_called_once_with(post_complete_details_dto=\
        post_empty_replies_complete_details_dto)
    assert actual_output == presenter_response


def test_get_post_with_duplicate_reactions_returns_post_details(
        post_duplicate_reactions_details_dto,
        post_duplicate_reactions_complete_details_dto,
        get_post_response):

    # Arrange
    presenter_response = get_post_response
    post_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = True
    storage.get_post_details_dto.return_value =\
        post_duplicate_reactions_details_dto
    presenter.get_response_for_get_post_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_post(post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    storage.get_post_details_dto.assert_called_once_with(post_id=post_id)
    presenter.get_response_for_get_post_details_dto\
        .assert_called_once_with(post_complete_details_dto=\
        post_duplicate_reactions_complete_details_dto)
    assert actual_output == presenter_response
