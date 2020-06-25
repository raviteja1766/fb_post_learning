import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.react_to_post_interactor\
    import ReactToPostInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist


def test_react_to_post_given_invalid_post_raises_exception():

    # Arrange
    user_id = 1
    post_id = 1
    reaction_type = ReactionType.HAHA.value

    post_storage = create_autospec(PostStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        post_storage=post_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    post_storage.validate_post_id.return_value = False
    presenter.raise_exception_for_invalid_post.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.react_to_post(
            user_id=user_id, post_id=post_id,
            reaction_type=reaction_type
        )

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    presenter.raise_exception_for_invalid_post.assert_called_once()

def test_react_to_post_given_valid_details_creates_reaction_to_post():

    # Arrange
    user_id = 1
    post_id = 1
    reaction_type = ReactionType.HAHA.value
    post_storage = create_autospec(PostStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        post_storage=post_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    post_storage.validate_post_id.return_value = True
    reaction_storage.get_old_post_reaction_if_exists\
        .side_effect = ReactionDoesNotExist

    # Act
    interactor.react_to_post(
        user_id=user_id, post_id=post_id, reaction_type=reaction_type
    )

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    reaction_storage.get_old_post_reaction_if_exists.assert_called_once_with(
        user_id=user_id, post_id=post_id)
    reaction_storage.react_to_post.assert_called_once_with(
        user_id=user_id, post_id=post_id, reaction_type=reaction_type)


def test_react_to_post_given_valid_details_updates_reaction_to_post():

    # Arrange
    user_id = 1
    post_id = 1
    old_reaction_type = ReactionType.WOW.value
    reaction_type = ReactionType.HAHA.value
    post_storage = create_autospec(PostStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        post_storage=post_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    post_storage.validate_post_id.return_value = True
    reaction_storage.get_old_post_reaction_if_exists\
        .return_value = old_reaction_type

    # Act
    interactor.react_to_post(user_id=user_id, post_id=post_id,
                             reaction_type=reaction_type)

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    reaction_storage.get_old_post_reaction_if_exists.assert_called_once_with(
        user_id=user_id, post_id=post_id)
    reaction_storage.update_post_reaction.assert_called_once_with(
        user_id=user_id, post_id=post_id, reaction_type=reaction_type
    )


def test_react_to_post_given_valid_details_undo_reaction_to_post():

    # Arrange
    user_id = 1
    post_id = 1
    old_reaction_type = ReactionType.HAHA.value
    reaction_type = ReactionType.HAHA.value
    post_storage = create_autospec(PostStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        post_storage=post_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    post_storage.validate_post_id.return_value = True
    reaction_storage.get_old_post_reaction_if_exists\
        .return_value = old_reaction_type

    # Act
    interactor.react_to_post(user_id=user_id, post_id=post_id,
                             reaction_type=reaction_type)

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    reaction_storage.get_old_post_reaction_if_exists.assert_called_once_with(
        user_id=user_id, post_id=post_id)
    reaction_storage.undo_post_reaction.assert_called_once_with(
        user_id=user_id, post_id=post_id
    )
