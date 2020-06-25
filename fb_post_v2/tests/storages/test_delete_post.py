import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation
from fb_post_v2.models import Post

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_delete_post_deletes_post(create_posts):
    
    # Arrange
    post_id = 2
    storage = PostStorageImplementation()
    
    # Act
    storage.delete_post(post_id=post_id)
    
    # Assert
    assert Post.objects.filter(id=2).exists() == False