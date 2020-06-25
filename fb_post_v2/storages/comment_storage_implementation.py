from django.contrib.admin.utils import flatten
from typing import Optional, List
from django.db.models import Count, Q, F, Prefetch
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.comment_storage_interface\
    import CommentStorageInterface
from fb_post_v2.interactors.storages.dtos import *
from fb_post_v2.models import Post, Comment, Reaction, User
from fb_post_v2.exceptions.exceptions import (
    InvalidPostException, InvalidCommentException,
    ReactionDoesNotExist
)

class CommentStorageImplementation(CommentStorageInterface):
    
    def validate_comment_id(self, comment_id: int):

        bool_field = Comment.objects.filter(id=comment_id).exists()
        return bool_field
    
    def create_comment(self, user_id: int, post_id: int,
                       comment_content: str) -> int:

        comment_obj = Comment.objects.create(post_id=post_id,
                                             content=comment_content,
                                             commented_by_id=user_id)
        return comment_obj.id
    
    def get_parent_comment_id(self, comment_id: int):

        comment_obj = Comment.objects.get(id=comment_id)
        return comment_obj.parent_comment_id
    
    def reply_to_comment(self, user_id: int, comment_id: int,
                         reply_content: str) -> int:

        comment_obj = Comment.objects.get(id=comment_id)
        post_id = comment_obj.post_id
        reply_obj = Comment.objects.create(
            commented_by_id=user_id, parent_comment_id=comment_id,
            post_id=post_id, content=reply_content
        )
        return reply_obj.id
    
    def get_replies_for_comment_details_dtos(self,
        comment_id: int) -> RepliesForCommentDetailsDto:
        
        reply_objs = Comment.objects\
            .filter(parent_comment_id=comment_id)\
            .select_related('commented_by')
        replys_dto = self._convert_comment_objs_to_dto(reply_objs)
        user_objs = self._get_user_objs_to_comments(reply_objs)
        users_dto = self._convert_user_objs_to_dtos(user_objs)
        return RepliesForCommentDetailsDto(
            users_dto=users_dto, replys_dto=replys_dto
        )
    
    @staticmethod
    def _get_user_objs_to_comments(comment_objs):
    
        return {
            comment_obj.commented_by for comment_obj in comment_objs
        }

    def _convert_comment_objs_to_dto(self, comment_objs):

        comments_dto = [
            self._convert_comment_obj_to_dto(comment_obj)
            for comment_obj in comment_objs
        ]
        return comments_dto
    
    def _convert_user_objs_to_dtos(self, user_objs):
        
        return [
            self._convert_user_obj_to_dto(user_obj)
            for user_obj in user_objs
        ]

    @staticmethod
    def _convert_comment_obj_to_dto(comment_obj):

        comment_dto = CommentDto(
            parent_comment_id=comment_obj.parent_comment_id,
            id=comment_obj.id, post_id=comment_obj.post_id,
            commented_by_id=comment_obj.commented_by_id,
            commented_at=(comment_obj.commented_at).replace(tzinfo=None),
            comment_content=comment_obj.content
        )
        return comment_dto
    
    @staticmethod
    def _convert_user_obj_to_dto(user_obj):

        user_dto = UserDto(
            id=user_obj.id, name=user_obj.name,
            profile_pic=user_obj.profile_pic
        )
        return user_dto