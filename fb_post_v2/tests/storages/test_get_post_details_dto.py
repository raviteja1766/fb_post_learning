import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation
from fb_post_v2.models import Post
from fb_post_v2.interactors.storages.dtos import PostDetailsDto

# def test_get_post_details_dto_given_valid_details_returns_post_details_dto(
#     create_replies, create_comment_reactions, create_post_reactions):
    
#     # Arrange
#     post_id = 1
#     storage = PostStorageImplementation()
    

#     pass