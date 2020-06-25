from fb_post.models import Reaction
from .validations import is_valid_post
from .get_post import get_user_details


def get_reactions_to_post(post_id):

    is_valid_post(post_id)
    reactions = Reaction.objects\
        .select_related('reacted_by')\
        .filter(post_id=post_id)

    reaction_list = [get_reaction_dict(reaction) for reaction in reactions]
    return reaction_list


def get_reaction_dict(reaction):

    reaction_dict = get_user_details(reaction.reacted_by)
    reaction_dict["reaction"] = reaction.reaction

    return reaction_dict
