import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation
from fb_post_v2.models import Comment

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_post_creates_post(create_posts):

    # Arrange
    user_id = 1
    post_id = 2
    comment_content = "comment_content_1"
    storage = CommentStorageImplementation()

    # Act
    comment_id = storage.create_comment(user_id=user_id, post_id=post_id,
                                        comment_content=comment_content)

    # Assert
    comment_obj = Comment.objects.get(id=comment_id)
    assert comment_obj.content == comment_content
    assert comment_obj.commented_by_id == user_id
    assert comment_obj.commented_at.strftime('%Y-%m-%d %X') ==\
        str(datetime(2012, 1, 13))
