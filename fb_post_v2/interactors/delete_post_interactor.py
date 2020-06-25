from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import Forbidden

class DeletePostInteractor:

    def __init__(self,storage=StorageInterface,
                 presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def delete_post(self, user_id: int, post_id: int):
        is_not_valid_post_id = not self.storage.validate_post_id(post_id)
        if is_not_valid_post_id:
            self.presenter.raise_exception_for_invalid_post()
            return
        posts_user_id = self.storage.get_user_of_post(post_id=post_id)
        is_post_posted_by_user = user_id == posts_user_id
        if is_post_posted_by_user:
            self.storage.delete_post(post_id=post_id)
        else:
            self.presenter.raise_exception_for_user_cannot_delete_post()
