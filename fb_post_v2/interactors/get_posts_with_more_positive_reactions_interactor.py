from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface

class GetPostsWithMorePositiveReactionsInteractor:

    def __init__(self,storage=StorageInterface,
                 presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_posts_with_more_positive_reactions(self):

        post_ids_list = self.storage.get_posts_with_more_positive_reactions()
        return self.presenter\
            .get_response_for_get_posts_with_more_positive_reactions(
                post_ids_list=post_ids_list
            )
