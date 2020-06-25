from unittest.mock import create_autospec
from fb_post_v2.interactors.get_posts_reacted_by_user_interactor\
    import GetPostsReactedByUserInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface


def test_get_posts_with_more_positive_reactions_returns_post_ids():

    # Arrange
    user_id = 1
    storage_output = [1,2,3]
    presenter_output = [1,2,3]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.get_posts_reacted_by_user.return_value = storage_output
    presenter.get_response_for_get_posts_reacted_by_user.\
        return_value = presenter_output
    interactor = GetPostsReactedByUserInteractor(
        storage=storage, presenter=presenter)

    # Act
    actual_output = interactor.get_posts_reacted_by_user(user_id=user_id)

    # Assert

    storage.get_posts_reacted_by_user.assert_called_once_with(user_id=user_id)
    presenter.get_response_for_get_posts_reacted_by_user.\
        assert_called_once_with(post_ids_list=storage_output)
    assert actual_output == presenter_output
