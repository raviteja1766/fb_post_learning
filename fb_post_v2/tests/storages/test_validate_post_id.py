import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage_implementation\
    import PostStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_post_id_given_invalid_post_id_returns_false():
    
    # Arrange
    post_id = 1
    storage = PostStorageImplementation()
    expected_output = False

    # Act
    actual_output = storage.validate_post_id(post_id=post_id)
    
    # Assert
    assert actual_output == expected_output
    

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_post_id_given_valid_post_id_returns_true(
        create_posts):
    
    # Arrange
    post_id = 2
    storage = PostStorageImplementation()
    expected_output = True

    # Act
    actual_output = storage.validate_post_id(post_id=post_id)
    
    # Assert
    assert actual_output == expected_output