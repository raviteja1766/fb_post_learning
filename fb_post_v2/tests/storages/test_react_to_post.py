import pytest
from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.storages.reaction_storage_implementation\
    import ReactionStorageImplementation
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.models import Reaction

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_react_to_post_creates_reaction_to_post(create_posts):
    
    # Arrange
    user_id = 1
    post_id = 1
    reaction_type = ReactionType.HAHA.value
    storage = ReactionStorageImplementation()
    expected_output = True
    
    # Act
    storage.react_to_post(user_id=user_id, post_id=post_id,
                          reaction_type=reaction_type)
    
    # Assert
    actual_output = Reaction.objects\
        .filter(reacted_by_id=user_id, post_id=post_id,
                reaction=reaction_type).exists()
    assert actual_output == expected_output