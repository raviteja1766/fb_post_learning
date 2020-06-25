from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface


class ReplyToCommentInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def reply_to_comment(self, user_id: int, comment_id: int,
                         reply_content: str):
        is_invalid_comment_id = not self.storage\
            .validate_comment_id(comment_id)
        if is_invalid_comment_id:
            self.presenter.raise_exception_for_invalid_comment()
            return
        parent_comment_id = self.storage.get_parent_comment_id(comment_id)
        if parent_comment_id:
            comment_id = parent_comment_id
        reply_id = self.storage.reply_to_comment(
            user_id=user_id, comment_id=comment_id,
            reply_content=reply_content
        )
        return self.presenter.get_reply_to_comment_response(reply_id=reply_id)
