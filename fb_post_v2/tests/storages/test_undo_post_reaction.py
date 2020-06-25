import pytest
from freezegun import freeze_time
from fb_post_v2.storages.reaction_storage_implementation\
    import ReactionStorageImplementation
from fb_post_v2.models import Reaction

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_undo_post_reaction_deletes_reaction_to_comment(
        create_post_reactions):
    
    # Arrange
    user_id = 1
    post_id = 1
    storage = ReactionStorageImplementation()
    expected_output = False
    
    # Act
    storage.undo_post_reaction(user_id=user_id, post_id=post_id)
    
    # Assert
    actual_output = Reaction.objects.filter(reacted_by_id=user_id,
                                            post_id=post_id).exists()
    assert expected_output == actual_output