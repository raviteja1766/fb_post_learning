from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from typing import List, Dict, Any

class GetReactionsToPostInteractor:

    def __init__(self, post_storage: PostStorageInterface,
                 reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface):
        self.post_storage = post_storage
        self.reaction_storage = reaction_storage
        self.presenter = presenter

    def get_reactions_to_post(self, post_id: int) -> List[Dict[str, Any]]:

        is_invalid_post_id = not self.post_storage\
            .validate_post_id(post_id=post_id)
        if is_invalid_post_id:
            self.presenter.raise_exception_for_invalid_post()
            return
        post_reactions_dtos = self.reaction_storage\
            .get_post_reactions_details_dto(post_id=post_id)
        return self.presenter.get_response_for_get_post_reactions_details_dto(
            post_reactions_dtos=post_reactions_dtos)
