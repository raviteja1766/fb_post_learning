from fb_post_v2.interactors.storages.post_storage_interface\
    import PostStorageInterface as StorageInterface
from fb_post_v2.interactors.presenters.presenterinterface\
    import PresenterInterface
from typing import List, Dict, Any
from collections import defaultdict
from fb_post_v2.dtos.dtos import *

class GetPostInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_post(self, post_id: int) -> Dict[str, Any]:
        is_invalid_post_id = not self.storage.validate_post_id(post_id=post_id)
        if is_invalid_post_id:
            self.presenter.raise_exception_for_invalid_post()
            return
        post_details_dto = self.storage.get_post_details_dto(post_id=post_id)
        reactions_dto = post_details_dto.reactions_dto
        posts_reactions_dict, posts_reactions_count_dict,\
        comments_reactions_dict, comments_reactions_count_dict =\
            self._get_reactions_dicts(reactions_dto)
        comments_dto = post_details_dto.comments_dto
        posts_comments_count_dict, comment_replies_count_dict,\
            = self._get_comments_dicts(comments_dto)
        comments_list_dict = self._get_comments_list_dict(comments_dto)
        post_reactions_dto, post_comments_dto, comments_reactions_dto,\
            comment_replies_count_dto = self._get_post_extra_details(
                post_id, comments_list_dict, posts_reactions_dict,
                posts_reactions_count_dict, posts_comments_count_dict,
                comments_reactions_dict, comments_reactions_count_dict,
                comment_replies_count_dict
            )
        post_complete_details_dto = self._get_post_complete_details_dto(
            post_details_dto, post_reactions_dto, post_comments_dto,
            comments_reactions_dto, comment_replies_count_dto)
        return self.presenter.get_response_for_get_post_details_dto(
            post_complete_details_dto=post_complete_details_dto)
            
            
    def _get_post_extra_details(
            self, post_id, comments_list_dict, posts_reactions_dict,
            posts_reactions_count_dict, posts_comments_count_dict,
            comments_reactions_dict, comments_reactions_count_dict,
            comment_replies_count_dict
        ):
        
        post_reactions_dto = self._get_post_reactions_dto(
            posts_reactions_dict, posts_reactions_count_dict, post_id
        )
        post_comments_dto = self._get_posts_comments_count_dict(
            posts_comments_count_dict, post_id
        )
        comments_list = comments_list_dict['comments']
        comments_reactions_dto = self._get_comment_reactions_dto(
            comments_list, comments_reactions_dict,
            comments_reactions_count_dict)
        parent_comments_list = comments_list_dict['parent_comments']
        comment_replies_count_dto = self._get_comments_replies_count(
            parent_comments_list, comment_replies_count_dict)
        return (post_reactions_dto, post_comments_dto, comments_reactions_dto,
            comment_replies_count_dto)
    
    @staticmethod
    def _get_comments_list_dict(comments_dto):
        
        comments_list_dict = defaultdict(list)
        for comment_dto in comments_dto:
            comments_list_dict['comments'].append(comment_dto.id)
            is_parent_comment = comment_dto.parent_comment_id == None
            if is_parent_comment:
                comments_list_dict['parent_comments'].append(comment_dto.id)
        return comments_list_dict
        
    
    @staticmethod
    def _get_post_complete_details_dto(post_details_dto, post_reactions_dto,
        post_comments_dto, comments_reactions_dto, comment_replies_count_dto):

        post_complete_details_dto = PostCompleteDetailsDto(
            post_dto=post_details_dto.post_dto,
            users_dto=post_details_dto.users_dto,
            comments_dto=post_details_dto.comments_dto,
            reactions_dto=post_details_dto.reactions_dto,
            post_reactions_dto=post_reactions_dto,
            post_comments_dto=post_comments_dto,
            comments_reactions_dto=comments_reactions_dto,
            comment_replies_count_dto=comment_replies_count_dto
        )
        return post_complete_details_dto
        
    @staticmethod
    def _get_comments_replies_count(comment_ids_list,
                                    comment_replies_count_dict):
        
        return [
            CommentRepliesCountDto(
                comment_id=comment_id,
                replies_count=comment_replies_count_dict.get(comment_id, 0)
            )
            for comment_id in comment_ids_list
        ]
    
    @staticmethod
    def _get_comment_reactions_dto(comment_ids_list, comments_reactions_dict,
                                   comments_reactions_count_dict):
        
        comments_reactions_list = [
            CommentReactionsDto(
                comment_id=comment_id,
                reactions_count=comments_reactions_count_dict.get(comment_id, 0),
                reactions=sorted(list(comments_reactions_dict.get(comment_id, [])))
            ) for comment_id in comment_ids_list
        ]
        return comments_reactions_list
        
        
    @staticmethod
    def _get_posts_comments_count_dict(posts_comments_count_dict, post_id):
        return PostCommentsCountDto(
            post_id=post_id, comments_count=posts_comments_count_dict.get(post_id, 0)
        )
        
    @staticmethod
    def _get_post_reactions_dto(posts_reactions_dict,
                                posts_reactions_count_dict, post_id):
        print(posts_reactions_dict, posts_reactions_count_dict, post_id)
        a = posts_reactions_dict.get(post_id)
        print(a)
        print("post id", post_id)
        b = posts_reactions_dict.get(1)
        print(b)
        post_reactions_dto = PostReactionsDto(
            post_id=post_id,
            reactions=sorted(list(posts_reactions_dict.get(post_id, []))),
            reactions_count=posts_reactions_count_dict.get(post_id, 0)
        )
        print(post_id)
        print(post_reactions_dto)
        return post_reactions_dto
    
    def _get_reactions_dicts(self, reactions_dto):
        
        posts_reactions_dict = defaultdict(set)
        posts_reactions_count_dict = defaultdict(int)
        comments_reactions_dict = defaultdict(set)
        comments_reactions_count_dict = defaultdict(int)
        for reaction in reactions_dto:
            if self._is_post_reaction(reaction):
                post_id = reaction.post_id
                posts_reactions_count_dict[post_id] += 1
                posts_reactions_dict[post_id].add(reaction.reaction)
            else:
                comment_id = reaction.comment_id
                comments_reactions_count_dict[comment_id] += 1
                comments_reactions_dict[comment_id].add(reaction.reaction)

        return (posts_reactions_dict, posts_reactions_count_dict,
                comments_reactions_dict, comments_reactions_count_dict)

    def _get_comments_dicts(self, comments_dto):
        
        comment_replies_count_dict = defaultdict(int)
        posts_comments_count_dict = defaultdict(int)
        for comment in comments_dto:
            if comment.parent_comment_id:
                comment_replies_count_dict[comment.parent_comment_id] += 1
            else:
                posts_comments_count_dict[comment.post_id] += 1
        
        return (
            posts_comments_count_dict,
            comment_replies_count_dict
        )

    @staticmethod    
    def _is_post_reaction(reaction):
        if reaction.post_id:
            return True
        return False
    