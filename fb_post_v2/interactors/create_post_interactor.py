from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface

class CreatePostInteractor:

    def __init__(self, post_storage: PostStorageInterface,
                 presenter: PresenterInterface):
        self.post_storage = post_storage
        self.presenter = presenter

    def create_post(self, user_id: int, post_content: str):
        
        new_post_id = self.post_storage.create_post(
            user_id = user_id, post_content = post_content
        )

        return self.presenter.get_create_post_response(
            post_id=new_post_id
        )
