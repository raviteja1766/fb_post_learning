import pytest
from freezegun import freeze_time
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation
from fb_post_v2.models import Comment
from datetime import datetime

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_parent_comment_id_given_valid_comment_id_returns_parent_id(
        create_comments):

    # Arrange
    comment_id = 2
    user_id = 1
    reply_content = "reply_1"
    storage = CommentStorageImplementation()

    # Act
    reply_id = storage.reply_to_comment(user_id=user_id,
        comment_id=comment_id, reply_content=reply_content)

    # Assert
    reply_obj = Comment.objects.get(id = reply_id)
    assert reply_obj.content == reply_content
    assert reply_obj.commented_by_id == user_id
    assert reply_obj.commented_at.strftime('%Y-%m-%d %X') ==\
        str(datetime(2012, 1, 13))
