from datetime import datetime

import pytest
from freezegun import freeze_time

from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import PostDto,\
    UserDto, CommentDto, ReactionDto
from fb_post_v2.models import User, Post, Comment, Reaction

@pytest.fixture()
def create_users():
    
    users_list = [
        {
            'name' : 'user_1',
            'profile_pic': 'profile_pic_1',
            'username': "username1"
        },
        {
            'name' : 'user_2',
            'profile_pic': 'profile_pic_2',
            'username': "username2"
        }
    ]
    user_instances_list = []
    for user in users_list:
        user_instances_list.append(
            User(name=user['name'],profile_pic=user['profile_pic'],
            username=user['username'])
        )
    User.objects.bulk_create(user_instances_list)


@pytest.fixture()
@freeze_time("2012-01-13")
def create_posts(create_users):
    posts_list = [
        {
            'content' : 'post_1',
            'posted_by_id': 1
        },
        {
            'content' : 'post_2',
            'posted_by_id': 2
        }
    ]
    post_instances_list = []
    for post in posts_list:
        post_instances_list.append(Post(content = post['content'],
        posted_by_id = post['posted_by_id']))
    Post.objects.bulk_create(post_instances_list)


@pytest.fixture()
@freeze_time("2012-01-13")
def create_comments(create_posts):
    
    comments_list = [
        {
            'content' : 'comment_1',
            'commented_by_id': 1,
            'post_id': 1
        },
        {
            'content' : 'comment_2',
            'commented_by_id': 2,
            'post_id': 2
        }
    ]
    comment_instances_list = []
    for comment in comments_list:
        comment_instances_list.append(
            Comment(content = comment['content'],
            commented_by_id = comment['commented_by_id'],
            post_id = comment['post_id']))
    Comment.objects.bulk_create(comment_instances_list)

@pytest.fixture()
@freeze_time("2012-01-13")
def create_replies(create_comments):
    replies = [
        {
            "commented_by_id": 1,
            "post_id": 1,
            "content": "reply1",
            "parent_comment_id": 2
        }
    ]
    comment_instances_list = []
    for comment in replies:
        comment_instances_list.append(
            Comment(content=comment['content'], post_id=comment['post_id'],
            commented_by_id=comment['commented_by_id'],
            parent_comment_id=comment['parent_comment_id']))
    Comment.objects.bulk_create(comment_instances_list)

@pytest.fixture()
@freeze_time("2012-01-13")
def create_post_reactions(create_posts):
    reactions_list = [
        {
            "post_id": 1,
            "reacted_by_id": 1,
            "reaction": "LIKE",
            "comment_id": None
        }
    ]
    reaction_instances_list = []
    for reaction in reactions_list:
        reaction_instances_list.append(
            Reaction(post_id = reaction['post_id'],
            comment_id = reaction['comment_id'],
            reaction = reaction['reaction'],
            reacted_by_id = reaction['reacted_by_id']))
    Reaction.objects.bulk_create(reaction_instances_list)


@pytest.fixture()
@freeze_time("2012-01-13")
def create_comment_reactions(create_comments):
    reactions = [
        {
            "post_id": None,
            "reacted_by_id": 1,
            "reaction": "SAD",
            "comment_id": 1
        }
    ]
    reaction_instances_list = []
    for reaction in reactions:
        reaction_instances_list.append(
            Reaction(post_id = reaction['post_id'],
            comment_id = reaction['comment_id'],
            reaction = reaction['reaction'],
            reacted_by_id = reaction['reacted_by_id']))
    Reaction.objects.bulk_create(reaction_instances_list)


# For get_post

@pytest.fixture()
def users_dto():
    return [
        UserDto(id=1,name="user_1",profile_pic="profile_pic_1"),
        UserDto(id=2,name="user_2",profile_pic="profile_pic_2")
    ]

# For more positive reactions

@pytest.fixture()
@freeze_time("2012-01-13")
def users():

    users_list = [
        {
            'name': 'user_1',
            'profile_pic': 'profile_pic_1',
            'username': "username1"
        },
        {
            'name': 'user_2',
            'profile_pic': 'profile_pic_2',
            'username': "username2"
        },
        {
            'name': 'user_3',
            'profile_pic': 'profile_pic_3',
            'username': "username3"
        },
        {
            'name': 'user_4',
            'profile_pic': 'profile_pic_4',
            'username': "username4"
        }
    ]
    user_instances_list = []
    for user in users_list:
        user_instances_list.append(User(
            name=user['name'],
            profile_pic=user['profile_pic'],
            username=user['username']
            )
        )
    User.objects.bulk_create(user_instances_list)


@pytest.fixture()
@freeze_time("2012-01-13")
def posts(users):

    posts_list = [
        {
            'content': 'post_1',
            'posted_by_id': 1
        },
        {
            'content': 'post_2',
            'posted_by_id': 2
        },
        {
            'content': 'post_3',
            'posted_by_id': 1
        },
        {
            'content': 'post_4',
            'posted_by_id': 2
        }
    ]
    post_instances_list = []
    for post in posts_list:
        post_instances_list.append(Post(
            content=post['content'],
            posted_by_id=post['posted_by_id']))
    Post.objects.bulk_create(post_instances_list)


@pytest.fixture()
@freeze_time("2012-01-13")
def comments(posts):

    comments_list = [
        {
            'content': 'comment_1',
            'commented_by_id': 2,
            'post_id': 1
        },
        {
            'content': 'comment_2',
            'commented_by_id': 3,
            'post_id': 1
        },
        {
            'content': 'comment_3',
            'commented_by_id': 1,
            'post_id': 2
        },
        {
            'content': 'comment_4',
            'commented_by_id': 3,
            'post_id': 2
        }
    ]
    comment_instances_list = []
    for comment in comments_list:
        comment_instances_list.append(
            Comment(content=comment['content'],
            commented_by_id=comment['commented_by_id'],
            post_id = comment['post_id']))
    Comment.objects.bulk_create(comment_instances_list)


@pytest.fixture()
@freeze_time("2012-01-13")
def reply_comments(users,posts,comments):
    Comment.objects.bulk_create([
        Comment(content='comment_5', commented_by_id=4, post_id=1,
                parent_comment_id=1),
        Comment(content='comment_6', commented_by_id=2, post_id=1,
                parent_comment_id=2)])


@pytest.fixture()
@freeze_time("2012-01-13")
def reactions(comments):
    
    reactions_list = [
        {
            'post_id': 1,
            'comment_id': None,
            'reaction': 'LOVE',
            'reacted_by_id':1
        },
        {
            'post_id': 1,
            'comment_id': None,
            'reaction': 'HAHA',
            'reacted_by_id':2
        },
        {
            'post_id': 1,
            'comment_id': None,
            'reaction': 'ANGRY',
            'reacted_by_id':3
        },
        {
            'post_id': 2,
            'comment_id': None,
            'reaction': 'SAD',
            'reacted_by_id': 1
        },
        {
            'post_id': 2,
            'comment_id': None,
            'reaction': 'THUMBS-DOWN',
            'reacted_by_id': 2
        },
        {
            'post_id': 2,
            'comment_id': None,
            'reaction': 'SAD',
            'reacted_by_id': 3
        },
        {
            'post_id': 3,
            'comment_id': None,
            'reaction': 'THUMBS-UP',
            'reacted_by_id': 3
        },
        {
            'post_id': None,
            'comment_id': 1,
            'reaction': 'SAD',
            'reacted_by_id': 2
        },
        {
            'post_id': None,
            'comment_id': 2,
            'reaction': 'SAD',
            'reacted_by_id': 2
        },
        {
            'post_id': None,
            'comment_id': 3,
            'reaction': 'SAD',
            'reacted_by_id': 1
        },
        {
            'post_id': None,
            'comment_id': 4,
            'reaction': 'HAHA',
            'reacted_by_id': 1
        }
    ]
    reaction_instances_list = []
    for reaction in reactions_list:
        reaction_instances_list.append(Reaction(
            post_id=reaction['post_id'],
            comment_id=reaction['comment_id'],
            reaction=reaction['reaction'],
            reacted_by_id=reaction['reacted_by_id']))
    Reaction.objects.bulk_create(reaction_instances_list)


@pytest.fixture()
@freeze_time("2012-01-13")
def negative_reactions(posts):

    negative_reactions_list = [
        {
            'post_id': 1,
            'comment_id': None,
            'reaction': 'SAD',
            'reacted_by_id':1
        },
        {
            'post_id': 1,
            'comment_id': None,
            'reaction': 'HAHA',
            'reacted_by_id':2
        },
        {
            'post_id': 1,
            'comment_id': None,
            'reaction': 'ANGRY',
            'reacted_by_id':3
        },
        {
            'post_id': 2,
            'comment_id': None,
            'reaction': 'WOW',
            'reacted_by_id': 1
        },
        {
            'post_id': 2,
            'comment_id': None,
            'reaction': 'THUMBS-DOWN',
            'reacted_by_id': 2
        },
        {
            'post_id': 2,
            'comment_id': None,
            'reaction': 'SAD',
            'reacted_by_id': 3
        },
        {
            'post_id': 3,
            'comment_id': None,
            'reaction': 'THUMBS-UP',
            'reacted_by_id': 3
        },
        {
            'post_id': 3,
            'comment_id': None,
            'reaction': 'THUMBS-DOWN',
            'reacted_by_id': 3
        }
    ]
    reaction_instances_list = []
    for reaction in negative_reactions_list:
        reaction_instances_list.append(Reaction(
            post_id=reaction['post_id'],
            comment_id=reaction['comment_id'],
            reaction=reaction['reaction'],
            reacted_by_id=reaction['reacted_by_id']))
    Reaction.objects.bulk_create(reaction_instances_list)


@pytest.fixture()
@freeze_time("2012-01-13")
def equal_reactions(comments):

    equal_reactions_list = [
        {
            'post_id': 1,
            'comment_id': None,
            'reaction': 'SAD',
            'reacted_by_id':1
        },
        {
            'post_id': 1,
            'comment_id': None,
            'reaction': 'HAHA',
            'reacted_by_id':2
        },
        {
            'post_id': 2,
            'comment_id': None,
            'reaction': 'WOW',
            'reacted_by_id': 1
        },
        {
            'post_id': 2,
            'comment_id': None,
            'reaction': 'ANGRY',
            'reacted_by_id': 2
        },
        {
            'post_id': 3,
            'comment_id': None,
            'reaction': 'THUMBS-UP',
            'reacted_by_id': 3
        },
        {
            'post_id': 3,
            'comment_id': None,
            'reaction': 'THUMBS-DOWN',
            'reacted_by_id': 3
        }
    ]
    reaction_instances_list = []
    for reaction in equal_reactions_list:
        reaction_instances_list.append(Reaction(
            post_id=reaction['post_id'],
            comment_id=reaction['comment_id'],
            reaction=reaction['reaction'],
            reacted_by_id=reaction['reacted_by_id']))
    Reaction.objects.bulk_create(reaction_instances_list)
