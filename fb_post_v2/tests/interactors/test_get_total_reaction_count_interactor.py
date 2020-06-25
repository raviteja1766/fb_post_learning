import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.get_total_reaction_count_interactor\
    import GetTotalReactionCountInteractor
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface

def test_get_total_reaction_count_when_there_are_some_reactions():

    # Arrange
    reaction_count = 5
    presenter_response = {
        "count": reaction_count
    }
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetTotalReactionCountInteractor(storage=storage,
                                                 presenter=presenter)
    storage.get_total_reaction_count.return_value = reaction_count
    presenter.get_total_reaction_count_response\
        .return_value = presenter_response

    # Act
    interactor_response = interactor.get_total_reaction_count()

    # Assert
    interactor_response['count'] == presenter_response['count']
    storage.get_total_reaction_count.assert_called_once()
    presenter.get_total_reaction_count_response\
        .assert_called_once_with(count=reaction_count)

