import pytest
from freezegun import freeze_time
from fb_post_v2.storages.comment_storage_implementation\
    import CommentStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_comment_id_given_invalid_comment_id_returns_false():

    # Arrange
    comment_id = 1
    storage = CommentStorageImplementation()
    expected_output = False

    # Act
    actual_output = storage.validate_comment_id(comment_id=comment_id)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_comment_id_given_valid_comment_id_returns_true(
        create_comments):

    # Arrange
    comment_id = 2
    storage = CommentStorageImplementation()
    expected_output = True

    # Act
    actual_output = storage.validate_comment_id(comment_id=comment_id)

    # Assert
    assert actual_output == expected_output