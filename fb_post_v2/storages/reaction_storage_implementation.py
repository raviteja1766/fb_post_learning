from django.contrib.admin.utils import flatten
from typing import Optional, List
from django.db.models import Count, Q, F, Prefetch
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.reaction_storage_interface\
    import ReactionStorageInterface
from fb_post_v2.interactors.storages.dtos import *
from fb_post_v2.models import Reaction
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist


class ReactionStorageImplementation(ReactionStorageInterface):
    
    def get_old_post_reaction_if_exists(self, user_id: int,
                                        post_id:int) -> ReactionType:

        try:
            reaction_obj = Reaction.objects.get(reacted_by_id=user_id,
                                                post_id=post_id)
        except Reaction.DoesNotExist:
            raise ReactionDoesNotExist
        return reaction_obj.reaction


    def get_old_comment_reaction_if_exists(self,
            user_id: int, comment_id:int) -> ReactionType:

        try:
            reaction_obj = Reaction.objects.get(reacted_by_id=user_id,
                                                comment_id=comment_id)
        except Reaction.DoesNotExist:
            raise ReactionDoesNotExist
        return reaction_obj.reaction

    def react_to_post(self, user_id: int, post_id: int,
                      reaction_type: ReactionType):

        Reaction.objects.create(reacted_by_id=user_id, post_id=post_id,
                                reaction=reaction_type)

    def undo_post_reaction(self, user_id: int, post_id: int):

        Reaction.objects.filter(reacted_by_id=user_id,
                                post_id=post_id).delete()

    def update_post_reaction(self, user_id: int, post_id: int,
        reaction_type: ReactionType):

        reaction_obj = Reaction.objects.get(
            reacted_by_id=user_id,post_id=post_id)
        reaction_obj.reaction = reaction_type
        reaction_obj.save()

    def react_to_comment(self, user_id: int, comment_id: int,
                      reaction_type: ReactionType):

        Reaction.objects.create(reacted_by_id=user_id, comment_id=comment_id,
                                reaction=reaction_type)

    def undo_comment_reaction(self, user_id: int, comment_id: int):

        Reaction.objects.filter(reacted_by_id=user_id,
                                comment_id=comment_id).delete()

    def update_comment_reaction(self, user_id: int, comment_id: int,
        reaction_type: ReactionType):

        reaction_obj = Reaction.objects.get(reacted_by_id=user_id,
                                            comment_id=comment_id)
        reaction_obj.reaction_type = reaction_type
        reaction_obj.save()

    def get_total_reaction_count(self) -> int:

        return Reaction.objects.all().count()

    def get_reaction_metrics_of_post_dto(self,
        post_id: int) -> List[ReactionMetricDto]:

        reaction_values_list = Reaction.objects\
            .filter(post_id=post_id)\
            .values_list('reaction')\
            .annotate(count=Count('id'))\
            .order_by('-count')

        reaction_metrics_of_post = [
            ReactionMetricDto(
                reaction_type=reaction.reaction,
                reaction_count=reaction.count
            )for reaction in reaction_values_list
        ]
        return reaction_metrics_of_post
    
    def get_post_reactions_details_dto(self,
        post_id: int) -> PostReactionCompleteDetailsDto:

        reactions_list = Reaction.objects\
            .select_related('reacted_by')\
            .filter(post_id=post_id)

        user_dtos = []
        reaction_dtos = []
        for reaction in reactions_list:
            user_dto = self._convert_user_obj_to_dto(reaction.reacted_by)
            reaction_dto = self._convert_reaction_obj_to_dto(reaction)
            user_dtos.append(user_dto)
            reaction_dtos.append(reaction_dto)

        return PostReactionCompleteDetailsDto(
            user_dtos=user_dtos, reaction_dtos=reaction_dtos
        )

    @staticmethod
    def _convert_user_obj_to_dto(user_obj):

        user_dto = UserDto(
            id=user_obj.id, name=user_obj.name,
            profile_pic=user_obj.profile_pic
        )
        return user_dto

    @staticmethod
    def _convert_reaction_obj_to_dto(reaction_obj):

        reaction_dto = ReactionDto(
            id=reaction_obj.id, comment_id=reaction_obj.comment_id,
            post_id=reaction_obj.post_id, reacted_by_id=reaction_obj.reacted_by_id,
            reaction=reaction_obj.reaction
        )
        return reaction_dto