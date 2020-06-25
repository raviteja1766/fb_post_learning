import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.get_reactions_to_post_interactor\
    import GetReactionsToPostInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
    PostReactionCompleteDetailsDto, UserDto, ReactionDto
)

def test_get_reactions_to_post_given_invalid_details_raises_invalid_post_id():

    # Arrange
    post_id = 1

    post_storage = create_autospec(PostStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetReactionsToPostInteractor(
        post_storage=post_storage, reaction_storage=reaction_storage,
        presenter=presenter
    )
    post_storage.validate_post_id.return_value = False
    presenter.raise_exception_for_invalid_post.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_reactions_to_post(post_id=post_id)

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    presenter.raise_exception_for_invalid_post.assert_called_once()

def test_get_reactions_to_post_given_valid_details_returns_post_reactions_details(
        user_dtos):

    # Arrange
    post_id = 1
    storage_response = PostReactionCompleteDetailsDto(
        user_dtos=user_dtos,
        reaction_dtos=[ReactionDto(
            id=1, post_id = 1, reacted_by_id = 1,
            comment_id=None, reaction = ReactionType.HAHA.value
        )]
    )
    presenter_response = [{
        "user_id": 1,
        "name": "raviteja",
        "profile_pic": "profile_pic1",
        "reaction": "HAHA"
    }]
    post_storage = create_autospec(PostStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetReactionsToPostInteractor(
        post_storage=post_storage, reaction_storage=reaction_storage,
        presenter=presenter
    )
    post_storage.validate_post_id.return_value = True
    reaction_storage.get_post_reactions_details_dto.return_value = storage_response
    presenter.get_response_for_get_post_reactions_details_dto.return_value =\
        presenter_response

    # Act
    actual_output = interactor.get_reactions_to_post(post_id=post_id)

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    reaction_storage.get_post_reactions_details_dto\
        .assert_called_once_with(post_id=post_id)
    presenter.get_response_for_get_post_reactions_details_dto.\
        assert_called_once_with(post_reactions_dtos=storage_response)
    assert actual_output == presenter_response
