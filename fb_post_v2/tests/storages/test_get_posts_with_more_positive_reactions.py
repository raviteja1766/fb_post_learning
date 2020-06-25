import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation
from fb_post_v2.models import Post

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_post_with_more_positive_reactions_when_more_positive_post_reactions_returns_post_ids_list(
        reactions):
    
    # Arrange
    storage = PostStorageImplementation()
    expected_post_ids_list = [1, 3]
    
    # Ask
    post_ids_list = storage.get_posts_with_more_positive_reactions()
    
    # Arrange
    assert post_ids_list == expected_post_ids_list


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_post_with_more_positive_reactions_when_more_negative_post_reactions_returns_post_ids_list(
        negative_reactions):
    
    # Arrange
    storage = PostStorageImplementation()
    expected_post_ids_list = [ ]
    
    # Ask
    post_ids_list = storage.get_posts_with_more_positive_reactions()
    
    # Arrange
    assert post_ids_list == expected_post_ids_list


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_post_with_more_positive_reactions_when_equal_post_reactions_returns_post_ids_list(
        equal_reactions):
    
    # Arrange
    storage = PostStorageImplementation()
    expected_post_ids_list = [ ]
    
    # Ask
    post_ids_list = storage.get_posts_with_more_positive_reactions()
    
    # Arrange
    assert post_ids_list == expected_post_ids_list