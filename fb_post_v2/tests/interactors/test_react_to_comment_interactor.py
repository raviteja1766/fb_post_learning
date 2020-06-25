import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.react_to_comment_interactor\
    import ReactToCommentInteractor
from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist


def test_react_to_comment_given_invalid_comment_raises_exception():

    # Arrange
    user_id = 1
    comment_id = 1
    reaction_type = ReactionType.HAHA.value

    comment_storage = create_autospec(CommentStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        comment_storage=comment_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    comment_storage.validate_comment_id.return_value = False
    presenter.raise_exception_for_invalid_comment.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.react_to_comment(
            user_id=user_id, comment_id=comment_id,
            reaction_type=reaction_type
        )

    # Assert
    comment_storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    presenter.raise_exception_for_invalid_comment.assert_called_once()

def test_react_to_comment_given_valid_details_creates_reaction_to_comment():

    # Arrange
    user_id = 1
    comment_id = 1
    reaction_type = ReactionType.HAHA.value
    comment_storage = create_autospec(CommentStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        comment_storage=comment_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    comment_storage.validate_comment_id.return_value = True
    reaction_storage.get_old_comment_reaction_if_exists\
        .side_effect = ReactionDoesNotExist

    # Act
    interactor.react_to_comment(
        user_id=user_id, comment_id=comment_id, reaction_type=reaction_type
    )

    # Assert
    comment_storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    reaction_storage.get_old_comment_reaction_if_exists.assert_called_once_with(
        user_id=user_id, comment_id=comment_id)
    reaction_storage.react_to_comment.assert_called_once_with(
        user_id=user_id, comment_id=comment_id, reaction_type=reaction_type)


def test_react_to_comment_given_valid_details_updates_reaction_to_comment():

    # Arrange
    user_id = 1
    comment_id = 1
    old_reaction_type = ReactionType.WOW.value
    reaction_type = ReactionType.HAHA.value
    comment_storage = create_autospec(CommentStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        comment_storage=comment_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    comment_storage.validate_comment_id.return_value = True
    reaction_storage.get_old_comment_reaction_if_exists\
        .return_value = old_reaction_type

    # Act
    interactor.react_to_comment(user_id=user_id, comment_id=comment_id,
                             reaction_type=reaction_type)

    # Assert
    comment_storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    reaction_storage.get_old_comment_reaction_if_exists.assert_called_once_with(
        user_id=user_id, comment_id=comment_id)
    reaction_storage.update_comment_reaction.assert_called_once_with(
        user_id=user_id, comment_id=comment_id, reaction_type=old_reaction_type
    )


def test_react_to_comment_given_valid_details_undo_reaction_to_comment():

    # Arrange
    user_id = 1
    comment_id = 1
    old_reaction_type = ReactionType.HAHA.value
    reaction_type = ReactionType.HAHA.value
    comment_storage = create_autospec(CommentStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        comment_storage=comment_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    comment_storage.validate_comment_id.return_value = True
    reaction_storage.get_old_comment_reaction_if_exists\
        .return_value = old_reaction_type

    # Act
    interactor.react_to_comment(user_id=user_id, comment_id=comment_id,
                             reaction_type=reaction_type)

    # Assert
    comment_storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    reaction_storage.get_old_comment_reaction_if_exists.assert_called_once_with(
        user_id=user_id, comment_id=comment_id)
    reaction_storage.undo_comment_reaction.assert_called_once_with(
        user_id=user_id, comment_id=comment_id
    )
