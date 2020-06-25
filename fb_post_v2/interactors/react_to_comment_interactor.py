from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist

class ReactToCommentInteractor:

    def __init__(self, comment_storage: CommentStorageInterface,
                 reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface):
        self.comment_storage = comment_storage
        self.reaction_storage = reaction_storage
        self.presenter = presenter

    def react_to_comment(self, user_id: int, comment_id: int,
                      reaction_type: ReactionType):

        is_invalid_comment_id = not self.comment_storage\
            .validate_comment_id(comment_id=comment_id)
        if is_invalid_comment_id:
            self.presenter.raise_exception_for_invalid_comment()
            return
        try:
            old_reaction_type = self.reaction_storage\
                .get_old_comment_reaction_if_exists(user_id=user_id,
                                                 comment_id=comment_id)
        except ReactionDoesNotExist:
            self.reaction_storage.react_to_comment(
                user_id=user_id, comment_id=comment_id, reaction_type=reaction_type)
            return
        is_same_reaction = old_reaction_type == reaction_type
        if is_same_reaction:
            self.reaction_storage.undo_comment_reaction(user_id=user_id,
                                                     comment_id=comment_id)
        else:
            self.reaction_storage.update_comment_reaction(
                user_id=user_id, comment_id=comment_id,
                reaction_type=old_reaction_type
            )