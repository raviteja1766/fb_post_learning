from presenters.presenter_implementation import PresenterImplementation
from storages.storage_implementation import StorageImplementation


class CreatePostInteractor:

    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def create_post(self, user_id: int,
                    post_content: str,
                    presenter: PresenterImplementation):
        self.storage.validate_post_id()
        post_id = self.storage.create_post(
            user_id=user_id,
            post_content=post_content
        )
        return presenter.get_create_post_response(post_id=post_id)
