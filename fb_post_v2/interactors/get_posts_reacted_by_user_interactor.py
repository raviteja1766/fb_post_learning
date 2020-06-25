from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from typing import List

class GetPostsReactedByUserInteractor:

    def __init__(self,storage=StorageInterface,
                 presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_posts_reacted_by_user(self, user_id: int) -> List[int]:

        post_ids_list = self.storage\
            .get_posts_reacted_by_user(user_id=user_id)
        return self.presenter\
            .get_response_for_get_posts_reacted_by_user(
                post_ids_list=post_ids_list
            )
