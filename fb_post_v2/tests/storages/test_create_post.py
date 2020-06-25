import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation
from fb_post_v2.models import Post

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_post_creates_post(create_users):

    # Arrange
    user_id = 1
    post_content = "post_content1"
    storage = PostStorageImplementation()

    # Act
    post_id = storage.create_post(user_id=user_id,
                                             post_content=post_content)

    # Assert
    post_obj = Post.objects.get(id=post_id)
    assert post_obj.content == post_content
    assert post_obj.posted_by_id == user_id
    assert post_obj.posted_at.strftime('%Y-%m-%d %X') ==\
        str(datetime(2012, 1, 13))