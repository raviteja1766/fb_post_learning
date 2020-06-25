import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.reaction_storage_implementation\
    import ReactionStorageImplementation
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_old_post_reaction_type_given_valid_details_creates_post(
        create_post_reactions):

    # Arrange
    user_id = 1
    post_id = 1
    storage = ReactionStorageImplementation()
    expected_reaction_type = "LIKE"

    # Act
    actual_reaction_type = storage.get_old_post_reaction_if_exists(
        user_id=user_id,post_id=post_id)

    # Assert
    assert actual_reaction_type == expected_reaction_type
    

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_old_comment_reaction_type_returns_exception_when_reaction_not_exists(
        create_post_reactions):

    # Arrange
    user_id = 1
    post_id = 2
    storage = ReactionStorageImplementation()

    # Act
    with pytest.raises(ReactionDoesNotExist):
        storage.get_old_post_reaction_if_exists(
            user_id=user_id,post_id=post_id)