import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.get_reaction_metrics_interactor\
    import GetReactionMetricsInteractor
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import ReactionMetricDto


def test_get_reaction_metrics_given_invalid_details_raises_invalid_post_id():

    # Arrange
    post_id = 1
    post_storage = create_autospec(PostStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetReactionMetricsInteractor(
        post_storage=post_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    post_storage.validate_post_id.return_value = False
    presenter.raise_exception_for_invalid_post.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_reaction_metrics(post_id=post_id)

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    presenter.raise_exception_for_invalid_post.assert_called_once()


def test_get_reaction_metrics_given_valid_details_returns_reaction_dict():

    # Arrange
    post_id = 1
    presenter_response = [
        {
            "reaction_type": "WOW",
            "reaction_count": 5
        },
        {
            "reaction_type": "HAHA",
            "reaction_count": 4
        }
    ]
    reaction_metrics_details_dto = [
        ReactionMetricDto(
            reaction_type=ReactionType.WOW.value,
            reaction_count=5),
        ReactionMetricDto(
            reaction_type=ReactionType.HAHA.value,
            reaction_count=4)
    ]

    post_storage = create_autospec(PostStorageInterface)
    reaction_storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetReactionMetricsInteractor(
        post_storage=post_storage, reaction_storage=reaction_storage,
        presenter=presenter)
    post_storage.validate_post_id.return_value = True
    reaction_storage.get_reaction_metrics_of_post_dto\
        .return_value = reaction_metrics_details_dto
    presenter.get_response_for_get_reaction_metrics_of_post\
        .return_value = presenter_response

    # Act
    interactor_response=interactor.get_reaction_metrics(post_id=post_id)

    # Assert
    post_storage.validate_post_id.assert_called_once_with(post_id=post_id)
    reaction_storage.get_reaction_metrics_of_post_dto\
        .assert_called_once_with(post_id=post_id)
    presenter.get_response_for_get_reaction_metrics_of_post\
        .assert_called_once_with(
            reaction_metrics_details_dto=reaction_metrics_details_dto
        )
    assert interactor_response == presenter_response
