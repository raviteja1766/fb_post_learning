import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation
from fb_post_v2.models import Post

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_posts_reacted_by_user_given_valid_details_returns_post_ids(
        reactions):
        
    # Arrange
    user_id = 1
    storage = PostStorageImplementation()
    expected_post_ids_list = [1, 2]
    
    # Act
    post_ids_list = storage.get_posts_reacted_by_user(user_id=user_id)
    
    # Arrange
    assert post_ids_list == expected_post_ids_list


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_posts_reacted_by_user_when_user_reacts_no_posts_returns_post_ids(
        reactions):
        
    # Arrange
    user_id = 4
    storage = PostStorageImplementation()
    expected_post_ids_list = []
    
    # Act
    post_ids_list = storage.get_posts_reacted_by_user(user_id=user_id)
    
    # Arrange
    assert post_ids_list == expected_post_ids_list