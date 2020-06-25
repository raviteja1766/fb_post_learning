from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from typing import List, Dict, Any

class GetRepliesForCommentInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_replies_for_comment(self, comment_id: int) -> List[Dict[str, Any]]:
        is_invalid_comment_id = not self.storage\
            .validate_comment_id(comment_id=comment_id)
        if is_invalid_comment_id:
            self.presenter.raise_exception_for_invalid_comment()
            return
        replies_details_dtos = self.storage\
            .get_replies_for_comment_details_dtos(comment_id=comment_id)
        return self.presenter\
            .get_response_for_get_replies_for_comment_details_dtos(
                replies_details_dtos=replies_details_dtos
            )
