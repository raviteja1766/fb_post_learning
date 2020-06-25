import pytest
from freezegun import freeze_time
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_parent_comment_id_given_valid_comment_id_returns_parent_id(
        create_replies):

    # Arrange
    comment_id = 3
    storage = CommentStorageImplementation()
    expected_parent_id = 2

    # Act
    actual_parent_id = storage.get_parent_comment_id(comment_id=comment_id)

    # Assert
    assert actual_parent_id == expected_parent_id
