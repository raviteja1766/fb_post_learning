from django.db import models
from fb_post.constants.reaction_type import ReactionType
from .user import User
from .post import Post
from .comment import Comment




class Reaction(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE,null = True)
    comment = models.ForeignKey(Comment,on_delete = models.CASCADE, null = True)
    reaction = models.CharField(
        max_length = 100,
        choices = [
            (reaction.value,reaction.name) for reaction in ReactionType
        ]
    )
    reacted_at = models.DateTimeField(auto_now = True)
    reacted_by = models.ForeignKey(User,on_delete = models.CASCADE)