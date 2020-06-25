from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from typing import Dict

class GetReactionMetricsInteractor:

    def __init__(self,post_storage=PostStorageInterface,
                 reaction_storage=ReactionStorageInterface,
                 presenter=PresenterInterface):
        self.reaction_storage = reaction_storage
        self.post_storage = post_storage
        self.presenter = presenter

    def get_reaction_metrics(self, post_id: int) -> Dict:

        is_not_valid_post_id = not self.post_storage.validate_post_id(post_id)
        if is_not_valid_post_id:
            self.presenter.raise_exception_for_invalid_post()
            return
        reaction_metrics_details_dto = self.reaction_storage\
            .get_reaction_metrics_of_post_dto(post_id=post_id)
        return self.presenter.get_response_for_get_reaction_metrics_of_post(
            reaction_metrics_details_dto=reaction_metrics_details_dto
        )