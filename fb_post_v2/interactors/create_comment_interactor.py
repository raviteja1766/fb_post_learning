from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface
from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface

class CreateCommentInteractor:

    def __init__(self,post_storage=PostStorageInterface,
                 comment_storage=CommentStorageInterface,
                 presenter=PresenterInterface):
        self.post_storage = post_storage
        self.comment_storage = comment_storage
        self.presenter = presenter

    def create_comment(self, user_id: int, post_id: int,
                       comment_content: str):
        is_invalid_post_id = not self.post_storage.validate_post_id(post_id)
        if is_invalid_post_id:
            self.presenter.raise_exception_for_invalid_post()
            return
        new_comment_id = self.comment_storage.create_comment(
            user_id=user_id, post_id=post_id,
            comment_content = comment_content
        )
        return self.presenter.get_create_comment_response(new_comment_id)
