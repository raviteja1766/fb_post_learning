from unittest.mock import create_autospec
from fb_post_v2.interactors.get_posts_with_more_positive_reactions_interactor\
    import GetPostsWithMorePositiveReactionsInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface


def test_get_posts_with_more_positive_reactions_returns_post_ids():

    # Arrange
    storage_output = [1,2,3]
    presenter_output = [1,2,3]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.get_posts_with_more_positive_reactions\
        .return_value = storage_output
    presenter.get_response_for_get_posts_with_more_positive_reactions.\
        return_value = presenter_output
    interactor = GetPostsWithMorePositiveReactionsInteractor(
        storage=storage, presenter=presenter)

    # Act
    actual_output = interactor.get_posts_with_more_positive_reactions()

    # Assert
    
    storage.get_posts_with_more_positive_reactions.assert_called_once()
    presenter.get_response_for_get_posts_with_more_positive_reactions.\
        assert_called_once_with(post_ids_list=storage_output)
    assert actual_output == presenter_output
