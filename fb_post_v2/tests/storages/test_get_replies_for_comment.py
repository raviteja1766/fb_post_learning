import pytest
from freezegun import freeze_time
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation
from fb_post_v2.models import Comment
from django.utils import timezone
from fb_post_v2.interactors.storages.dtos import (
    UserDto, CommentDto,RepliesForCommentDetailsDto
)
from datetime import datetime

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_replies_for_comment_given_valid_returns_replies_dtos(
        create_replies):

    # Arrange
    comment_id = 2
    expected_response = RepliesForCommentDetailsDto(
        users_dto=[
            UserDto(id=1,name="user_1",profile_pic="profile_pic_1")
        ],
        replys_dto=[
            CommentDto(id=3,
            commented_by_id=1,
            post_id=1,
            comment_content="reply1",
            commented_at=datetime(2012,1,13),
            parent_comment_id=2)
        ]
    )
    storage = CommentStorageImplementation()

    # Act
    actual_response = storage.get_replies_for_comment_details_dtos(
        comment_id=comment_id
    )


    # Assert
    assert actual_response.users_dto == expected_response.users_dto
    assert actual_response.replys_dto == expected_response.replys_dto