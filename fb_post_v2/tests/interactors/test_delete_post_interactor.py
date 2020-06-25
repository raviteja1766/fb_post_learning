import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.delete_post_interactor\
    import DeletePostInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import Forbidden, NotFound


def test_delete_post_given_invalid_details_raises_invalid_post_id():

    # Arrange
    user_id = 1
    post_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeletePostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = False
    presenter.raise_exception_for_invalid_post.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_post(user_id=user_id, post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    presenter.raise_exception_for_invalid_post.assert_called_once()


def test_delete_post_given_invalid_details_raises_user_cannot_delete_post():

    # Arrange
    user_id = 1
    posts_user_id = 2
    post_id = 3

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeletePostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = True
    storage.get_user_of_post.return_value = posts_user_id
    presenter.raise_exception_for_user_cannot_delete_post\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.delete_post(user_id=user_id, post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    storage.get_user_of_post.assert_called_once_with(post_id=post_id)
    presenter.raise_exception_for_user_cannot_delete_post.assert_called_once()


def test_delete_post_given_valid_details_deletes_post():

    # Arrange
    user_id = 1
    post_id = 3

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeletePostInteractor(storage=storage,presenter=presenter)
    storage.validate_post_id.return_value = True
    storage.get_user_of_post.return_value = user_id

    # Act
    interactor.delete_post(user_id=user_id, post_id=post_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=post_id)
    storage.get_user_of_post.assert_called_once_with(post_id=post_id)
    storage.delete_post.assert_called_once_with(post_id=post_id)