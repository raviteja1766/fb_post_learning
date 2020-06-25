import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation
from fb_post_v2.models import Post

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_user_of_post_returns_user_id(create_posts):
    
    # Arrange
    post_id = 2
    user_id = 2
    storage = PostStorageImplementation()
    
    # Act
    response_user_id = storage.get_user_of_post(post_id=post_id)
    
    # Assert
    assert response_user_id == user_id