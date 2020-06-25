import enum
from datetime import datetime
import factory, factory.django
from django.db import models
from fb_post_v2.models import *
from fb_post_v2.constants.enums import ReactionType

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: "user_%d" % n)
    profile_pic = factory.Sequence(lambda n: "profile_pic_%d" % n)
    username = factory.Sequence(lambda n: "username%d" % n)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    content = factory.Sequence(lambda n: "post_%d" % n)
    posted_at = factory.LazyFunction(datetime.now)
    posted_by = factory.Iterator(User.objects.all())


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Sequence(lambda n: "comment_%d" % n)
    commented_at = factory.LazyFunction(datetime.now)
    commented_by = factory.Iterator(User.objects.all())
    post = factory.Iterator(Post.objects.all())
    parent_comment = None


class ReplyFactory(CommentFactory):
    parent_comment = factory.Iterator(
        Comment.objects.filter(parent_comment_id=None)
    )
    post = factory.LazyAttribute(lambda o: o.parent_comment.post)


class PostReactionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Reaction

    post = factory.Iterator(Post.objects.all())
    reacted_at = factory.LazyFunction(datetime.now)
    reaction = factory.Iterator([
        reaction.value for reaction in ReactionType
    ])
    reacted_by = factory.Iterator(User.objects.all())


class CommentReactionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Reaction

    comment = factory.Iterator(Comment.objects.all())
    reacted_at = factory.LazyFunction(datetime.now)
    reaction = factory.Iterator([
        reaction.value for reaction in ReactionType
    ])
    reacted_by = factory.Iterator(User.objects.all())

