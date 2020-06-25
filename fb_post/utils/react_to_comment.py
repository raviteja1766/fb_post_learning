from fb_post.models import Reaction
from .validations import (
    is_valid_user, is_valid_comment, is_valid_reaction_type
)


def react_to_comment(user_id, comment_id, reaction_type):

    is_valid_user(user_id)
    is_valid_comment(comment_id)
    is_valid_reaction_type(reaction_type)
    try:
        reaction_obj = Reaction.objects.get(
            reacted_by_id=user_id, comment_id=comment_id
        )
    except Reaction.DoesNotExist:
        Reaction.objects.create(
            comment_id=comment_id,
            reaction=reaction_type,
            reacted_by_id=user_id
        )
        return
    compare_reaction_object_with_reaction_type(reaction_obj, reaction_type)


def compare_reaction_object_with_reaction_type(reaction_obj, reaction_type):

    is_undo_reaction = reaction_obj.reaction == reaction_type

    if is_undo_reaction:
        reaction_obj.delete()
    else:
        update_reaction_type_in_reaction_obj(reaction_obj, reaction_type)


def update_reaction_type_in_reaction_obj(reaction_obj, reaction_type):

    reaction_obj.reaction = reaction_type
    reaction_obj.save()
