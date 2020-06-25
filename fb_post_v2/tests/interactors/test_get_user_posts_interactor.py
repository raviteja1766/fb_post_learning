import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.get_user_posts_interactor\
    import GetUserPostsInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from fb_post_v2.dtos.dtos import UserPostsCompleteDetailsDto


def test_get_user_posts_given_valid_details_returns_post_details(
        user_posts_details_dto, user_posts_complete_details_dto,
        get_user_posts_response
    ):

    # Arrange
    presenter_response = get_user_posts_response
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage=storage,presenter=presenter)
    storage.get_user_posts_details_dto.return_value =\
        user_posts_details_dto
    presenter.get_response_for_get_user_posts_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_user_posts(user_id=user_id)

    # Assert
    storage.get_user_posts_details_dto\
        .assert_called_once_with(user_id=user_id)
    presenter.get_response_for_get_user_posts_details_dto\
        .assert_called_once_with(
            user_posts_complete_details_dto=user_posts_complete_details_dto
        )
    assert actual_output == presenter_response


def test_get_user_posts_with_no_comments_returns_post_details(
        user_posts_comments_empty_details_dto,
        user_posts_comments_empty_complete_details_dto,
        get_user_posts_response
    ):

    # Arrange
    presenter_response = get_user_posts_response
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage=storage,presenter=presenter)
    storage.get_user_posts_details_dto.return_value =\
        user_posts_comments_empty_details_dto
    presenter.get_response_for_get_user_posts_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_user_posts(user_id=user_id)

    # Assert
    storage.get_user_posts_details_dto\
        .assert_called_once_with(user_id=user_id)
    presenter.get_response_for_get_user_posts_details_dto\
        .assert_called_once_with(
            user_posts_complete_details_dto=\
            user_posts_comments_empty_complete_details_dto
        )
    assert actual_output == presenter_response


def test_get_user_posts_with_no_post_reactions_returns_post_details(
        user_posts_empty_reactions_details_dto,
        user_posts_empty_reactions_complete_details_dto,
        get_user_posts_response
    ):

    # Arrange
    presenter_response = get_user_posts_response
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage=storage,presenter=presenter)
    storage.get_user_posts_details_dto.return_value =\
        user_posts_empty_reactions_details_dto
    presenter.get_response_for_get_user_posts_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_user_posts(user_id=user_id)

    # Assert
    storage.get_user_posts_details_dto\
        .assert_called_once_with(user_id=user_id)
    presenter.get_response_for_get_user_posts_details_dto\
        .assert_called_once_with(
            user_posts_complete_details_dto=\
            user_posts_empty_reactions_complete_details_dto
        )
    assert actual_output == presenter_response


def test_get_user_posts_with_comments_empty_reactions_returns_post_details(
        user_posts_comments_empty_reactions_details_dto,
        user_posts_comments_empty_reactions_complete_details_dto,
        get_user_posts_response
    ):

    # Arrange
    presenter_response = get_user_posts_response
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage=storage,presenter=presenter)
    storage.get_user_posts_details_dto.return_value =\
        user_posts_comments_empty_reactions_details_dto
    presenter.get_response_for_get_user_posts_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_user_posts(user_id=user_id)

    # Assert
    storage.get_user_posts_details_dto\
        .assert_called_once_with(user_id=user_id)
    presenter.get_response_for_get_user_posts_details_dto\
        .assert_called_once_with(
            user_posts_complete_details_dto=\
            user_posts_comments_empty_reactions_complete_details_dto
        )
    assert actual_output == presenter_response

def test_get_user_posts_with_empty_replies_returns_post_details(
        user_posts_empty_replies_details_dto,
        user_posts_empty_replies_complete_details_dto,
        get_user_posts_response
    ):

    # Arrange
    presenter_response = get_user_posts_response
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage=storage,presenter=presenter)
    storage.get_user_posts_details_dto.return_value =\
        user_posts_empty_replies_details_dto
    presenter.get_response_for_get_user_posts_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_user_posts(user_id=user_id)

    # Assert
    storage.get_user_posts_details_dto\
        .assert_called_once_with(user_id=user_id)
    presenter.get_response_for_get_user_posts_details_dto\
        .assert_called_once_with(
            user_posts_complete_details_dto=\
            user_posts_empty_replies_complete_details_dto
        )
    assert actual_output == presenter_response


def test_get_user_posts_with_duplicate_reactions_returns_post_details(
        user_posts_duplicate_reactionsdetails_dto,
        user_posts_duplicate_reactions_complete_details_dto,
        get_user_posts_response
    ):

    # Arrange
    presenter_response = get_user_posts_response
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage=storage,presenter=presenter)
    storage.get_user_posts_details_dto.return_value =\
        user_posts_duplicate_reactionsdetails_dto
    presenter.get_response_for_get_user_posts_details_dto\
        .return_value = presenter_response

    # Act
    actual_output = interactor.get_user_posts(user_id=user_id)

    # Assert
    storage.get_user_posts_details_dto\
        .assert_called_once_with(user_id=user_id)
    presenter.get_response_for_get_user_posts_details_dto\
        .assert_called_once_with(
            user_posts_complete_details_dto=\
            user_posts_duplicate_reactions_complete_details_dto
        )
    assert actual_output == presenter_response