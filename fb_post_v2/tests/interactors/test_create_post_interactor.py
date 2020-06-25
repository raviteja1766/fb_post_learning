from unittest.mock import create_autospec

from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface


def test_create_post_given_valid_details_returns_post_id():

    # Arrange
    user_id = 1
    post_content = "Nice Post"
    post_id = 3
    presenter_response = {
        "post_id": post_id
    }
    presenter = create_autospec(PresenterInterface)
    post_storage = create_autospec(PostStorageInterface)
    interactor = CreatePostInteractor(post_storage=post_storage,
                                      presenter=presenter)
    post_storage.create_post.return_value = post_id
    presenter.get_create_post_response.return_value = presenter_response

    # Act
    interactor_response = interactor.create_post(
        user_id=user_id,
        post_content=post_content,
    )

    # Assert
    post_storage.create_post.assert_called_once_with(
        user_id=user_id,
        post_content=post_content)
    presenter.get_create_post_response.assert_called_once_with(
        post_id=post_id)
    assert interactor_response['post_id'] == presenter_response['post_id']
