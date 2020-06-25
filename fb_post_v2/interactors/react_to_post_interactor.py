from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist

class ReactToPostInteractor:

    def __init__(self, post_storage: PostStorageInterface,
                 reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface):
        self.post_storage = post_storage
        self.reaction_storage = reaction_storage
        self.presenter = presenter

    def react_to_post(self, user_id: int, post_id: int,
                      reaction_type: ReactionType):

        is_invalid_post_id = not self.post_storage\
            .validate_post_id(post_id=post_id)
        if is_invalid_post_id:
            self.presenter.raise_exception_for_invalid_post()
            return
        try:
            old_reaction_type = self.reaction_storage\
                .get_old_post_reaction_if_exists(user_id=user_id,
                                                 post_id=post_id)
        except ReactionDoesNotExist:
            self.reaction_storage.react_to_post(
                user_id=user_id, post_id=post_id, reaction_type=reaction_type)
            return
        is_same_reaction = old_reaction_type == reaction_type
        if is_same_reaction:
            self.reaction_storage.undo_post_reaction(user_id=user_id,
                                                     post_id=post_id)
        else:
            self.reaction_storage.update_post_reaction(
                user_id=user_id, post_id=post_id,
                reaction_type=reaction_type
            )
