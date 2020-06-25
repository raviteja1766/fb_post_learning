from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface


class GetTotalReactionCountInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_total_reaction_count(self):

        reaction_count = self.storage.get_total_reaction_count()
        return self.presenter.get_total_reaction_count_response(
            count=reaction_count
        )
