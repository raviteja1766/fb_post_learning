from datetime import datetime

import pytest

from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import *
from fb_post_v2.dtos.dtos import *

# Input dtos

@pytest.fixture()
def user_dtos():
    user_dtos = [
        UserDto(id=1,name="raviteja",profile_pic="profile_pic1"),
        UserDto(id=2,name="suryateja",profile_pic="profile_pic2")
    ]
    return user_dtos


@pytest.fixture()
def reaction_dtos():
    reaction_dtos = [
        ReactionDto(
            id=1, post_id = 1, reacted_by_id = 1,
            comment_id=None, reaction = ReactionType.HAHA.value
        ),
        ReactionDto(
            id=2, post_id = None, reacted_by_id = 1,
            comment_id=1, reaction = ReactionType.WOW.value
        ),
        ReactionDto(
            id=3, post_id = None, reacted_by_id = 2,
            comment_id=2, reaction = ReactionType.ANGRY.value
        )
    ]
    return reaction_dtos

@pytest.fixture()
def post_reactions_empty_dtos():
    reaction_dtos = [
        ReactionDto(
            id=1, post_id = None, reacted_by_id = 1,
            comment_id=1, reaction = ReactionType.WOW.value
        ),
        ReactionDto(
            id=2, post_id = None, reacted_by_id = 2,
            comment_id=2, reaction = ReactionType.ANGRY.value
        )
    ]
    return reaction_dtos

@pytest.fixture()
def comment_reactions_empty_dtos():
    reaction_dtos = [
        ReactionDto(
            id=1, post_id = 1, reacted_by_id = 1,
            comment_id=None, reaction = ReactionType.HAHA.value
        ),
        ReactionDto(
            id=3, post_id = None, reacted_by_id = 2,
            comment_id=2, reaction = ReactionType.ANGRY.value
        )
    ]
    return reaction_dtos


@pytest.fixture()
def comment_dtos():
    comment_dtos = [CommentDto(id=1,
                               commented_by_id=2,
                               post_id=1,
                               comment_content="hii",
                               commented_at=datetime(2019, 4, 22, 0, 0),
                               parent_comment_id=None),
                    CommentDto(id=2,
                               commented_by_id=2,
                               post_id=None,
                               comment_content="hii ra",
                               commented_at=datetime(2019, 4, 22, 0, 0),
                               parent_comment_id=1)
                    ]
    return comment_dtos

# test 2


@pytest.fixture()
def post_dto():
    post_dtos = PostDto(id=1,
                        post_content="My Post Content",
                        posted_at=datetime(2019, 4, 22, 0, 0),
                        posted_by_id=1)
    return post_dtos


@pytest.fixture()
def post_dtos():
    post_dtos = [
        PostDto(
            id=1, post_content="My Post Content",
            posted_at=datetime(2019, 4, 22, 0, 0), posted_by_id=1
        )
    ]
    return post_dtos


# Output Dtos


@pytest.fixture()
def post_reactions_dto():
    post_reactions_dto = PostReactionsDto(
        post_id=1,reactions=["HAHA"],reactions_count=1
    )
    return post_reactions_dto

@pytest.fixture()
def posts_reactions_dto():
    post_reactions_dto = [PostReactionsDto(
        post_id=1,reactions=["HAHA"],reactions_count=1
    )]
    return post_reactions_dto

@pytest.fixture()
def post_comments_dto():
    return PostCommentsCountDto(post_id=1, comments_count=1)

@pytest.fixture()
def posts_comments_dto():
    return [PostCommentsCountDto(post_id=1, comments_count=1)]

@pytest.fixture()
def comments_reactions_dto():
    return [
        CommentReactionsDto(comment_id=1, reactions=["WOW"], reactions_count=1),
        CommentReactionsDto(comment_id=2, reactions=["ANGRY"], reactions_count=1)
    ]

@pytest.fixture()
def comment_replies_count_dto():
    return [
        CommentRepliesCountDto(comment_id=1, replies_count=1)
    ]



# test 2

@pytest.fixture()
def post_details_dto(post_dto,user_dtos,comment_dtos,reaction_dtos):
    post_details_dto = PostDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=reaction_dtos
    )
    return post_details_dto

@pytest.fixture()
def post_complete_details_dto(
        post_dto,user_dtos,comment_dtos,reaction_dtos,post_reactions_dto,
        post_comments_dto, comments_reactions_dto, comment_replies_count_dto
    ):
    post_details_dto = PostCompleteDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=reaction_dtos,
        post_reactions_dto=post_reactions_dto,
        post_comments_dto=post_comments_dto,
        comments_reactions_dto=comments_reactions_dto,
        comment_replies_count_dto=comment_replies_count_dto
    )
    return post_details_dto



# test 3

@pytest.fixture()
def post_comments_empty_storage_dtos():
    comment_dtos = []
    return comment_dtos

@pytest.fixture()
def post_comments_empty_dtos():
    return PostCommentsCountDto(post_id=1, comments_count=0)

@pytest.fixture()
def posts_comments_empty_dtos():
    return [PostCommentsCountDto(post_id=1, comments_count=0)]

@pytest.fixture()
def comment_empty_reactions():
    return []

@pytest.fixture()
def comment_empty_replies():

    return []

@pytest.fixture()
def post_empty_comment_reactions():
    
    reaction_dtos = [
        ReactionDto(
            id=1, post_id = 1, reacted_by_id = 1,
            comment_id=None, reaction = ReactionType.HAHA.value
        )
    ]
    return reaction_dtos
    
    
@pytest.fixture()
def post_empty_comments_details_dto(
        post_dto,user_dtos,post_comments_empty_storage_dtos,
        post_empty_comment_reactions):
    post_details_dto = PostDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=post_comments_empty_storage_dtos,
        reactions_dto=post_empty_comment_reactions
    )
    return post_details_dto

@pytest.fixture()
def post_empty_comments_complete_details_dto(
        post_dto,user_dtos,post_comments_empty_dtos,post_empty_comment_reactions,
        post_reactions_dto,comment_empty_reactions,
        post_comments_empty_storage_dtos, comment_empty_replies
    ):
    post_details_dto = PostCompleteDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=post_comments_empty_storage_dtos,
        reactions_dto=post_empty_comment_reactions,
        post_reactions_dto=post_reactions_dto,
        post_comments_dto=post_comments_empty_dtos,
        comments_reactions_dto=comment_empty_reactions,
        comment_replies_count_dto=comment_empty_replies
    )
    return post_details_dto

@pytest.fixture()
def user_posts_comments_empty_details_dto(post_dtos,user_dtos,
        post_comments_empty_storage_dtos,post_empty_comment_reactions):
    post_details_dto = UserPostsDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=post_comments_empty_storage_dtos,
        reactions_dto=post_empty_comment_reactions
    )
    return post_details_dto

@pytest.fixture()
def user_posts_comments_empty_complete_details_dto(
        post_dtos,user_dtos,post_comments_empty_storage_dtos,post_empty_comment_reactions,
        posts_reactions_dto, posts_comments_empty_dtos, comment_empty_reactions,
        comment_empty_replies
    ):
    post_details_dto = UserPostsCompleteDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=post_comments_empty_storage_dtos,
        reactions_dto=post_empty_comment_reactions,
        posts_reactions_dto=posts_reactions_dto,
        posts_comments_dto=posts_comments_empty_dtos,
        comments_reactions_dto=comment_empty_reactions,
        comment_replies_count_dto=comment_empty_replies
    )
    return post_details_dto



# test 4

@pytest.fixture()
def post_empty_reactions():
    reaction_dtos = [
        ReactionDto(
            id=1, post_id = None, reacted_by_id = 1,
            comment_id=1, reaction = ReactionType.WOW.value
        ),
        ReactionDto(
            id=2, post_id = None, reacted_by_id = 2,
            comment_id=2, reaction = ReactionType.ANGRY.value
        )
    ]
    return reaction_dtos
    

@pytest.fixture()
def post_empty_reactions_details_dto(post_dto,user_dtos,
        comment_dtos,post_empty_reactions):
    post_details_dto = PostDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=post_empty_reactions
    )
    return post_details_dto

@pytest.fixture()
def post_empty_reactions_dto():
    return PostReactionsDto(
                post_id=1, reactions=[], reactions_count=0)

@pytest.fixture()
def posts_empty_reactions_dto():
    return [PostReactionsDto(
                post_id=1, reactions=[], reactions_count=0)]

@pytest.fixture()
def post_empty_reactions_complete_details_dto(
        post_dto,user_dtos,comment_dtos,post_empty_reactions,
        post_empty_reactions_dto, post_comments_dto, comments_reactions_dto,
        comment_replies_count_dto
    ):
    post_details_dto = PostCompleteDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=post_empty_reactions,
        post_reactions_dto=post_empty_reactions_dto,
        post_comments_dto=post_comments_dto,
        comments_reactions_dto=comments_reactions_dto,
        comment_replies_count_dto=comment_replies_count_dto
    )
    return post_details_dto

@pytest.fixture()
def user_posts_empty_reactions_details_dto(
        post_dtos,user_dtos,comment_dtos,post_empty_reactions):
    post_details_dto = UserPostsDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=post_empty_reactions
    )
    return post_details_dto

@pytest.fixture()
def user_posts_empty_reactions_complete_details_dto(
        post_dtos,user_dtos,comment_dtos,post_empty_reactions,
        posts_empty_reactions_dto, posts_comments_dto,
        comments_reactions_dto, comment_replies_count_dto
    ):
    post_details_dto = UserPostsCompleteDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=post_empty_reactions,
        posts_reactions_dto=posts_empty_reactions_dto,
        posts_comments_dto=posts_comments_dto,
        comments_reactions_dto=comments_reactions_dto,
        comment_replies_count_dto=comment_replies_count_dto
    )
    return post_details_dto
    
    
# task-5

@pytest.fixture()
def comment_storage_empty_reactions():
    
    reaction_dtos = [
        ReactionDto(
            id=1, post_id = 1, reacted_by_id = 1,
            comment_id=None, reaction = ReactionType.HAHA.value
        ),
        ReactionDto(
            id=2, post_id = None, reacted_by_id = 2,
            comment_id=2, reaction = ReactionType.ANGRY.value
        )
    ]
    return reaction_dtos

@pytest.fixture()
def parent_comment_empty_reactions():
    
    return [
        CommentReactionsDto(comment_id=1, reactions=[], reactions_count=0),
        CommentReactionsDto(comment_id=2, reactions=["ANGRY"], reactions_count=1)
    ]
    

@pytest.fixture()
def post_comment_empty_reactions_details_dto(post_dto,user_dtos,
        comment_dtos,comment_storage_empty_reactions):
    post_details_dto = PostDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=comment_storage_empty_reactions
    )
    return post_details_dto

@pytest.fixture()
def post_comment_empty_reactions_complete_details_dto(
        post_dto,user_dtos,comment_dtos,comment_storage_empty_reactions,
        post_reactions_dto, post_comments_dto,
        parent_comment_empty_reactions,
        comment_replies_count_dto
    ):
    post_details_dto = PostCompleteDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=comment_storage_empty_reactions,
        post_reactions_dto=post_reactions_dto,
        post_comments_dto=post_comments_dto,
        comments_reactions_dto=parent_comment_empty_reactions,
        comment_replies_count_dto=comment_replies_count_dto
    )
    return post_details_dto

@pytest.fixture()
def user_posts_comments_empty_reactions_details_dto(post_dtos,user_dtos,
        comment_dtos, comment_storage_empty_reactions):
    post_details_dto = UserPostsDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=comment_storage_empty_reactions
    )
    return post_details_dto

@pytest.fixture()
def user_posts_comments_empty_reactions_complete_details_dto(
        post_dtos,user_dtos,comment_dtos,comment_storage_empty_reactions,
        posts_reactions_dto, parent_comment_empty_reactions,
        posts_comments_dto, comment_replies_count_dto
    ):
    post_details_dto = UserPostsCompleteDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=comment_storage_empty_reactions,
        posts_reactions_dto=posts_reactions_dto,
        posts_comments_dto=posts_comments_dto,
        comments_reactions_dto=parent_comment_empty_reactions,
        comment_replies_count_dto=comment_replies_count_dto
    )
    return post_details_dto

    
# test 6
@pytest.fixture()
def post_comments_empty_replies_dtos():
    comment_dtos = [
        CommentDto(
            id=1,
            commented_by_id=2,
            post_id=1,
            comment_content="hii",
            commented_at=datetime(2019, 4, 22, 0, 0),
            parent_comment_id=None
        )
    ]
    return comment_dtos

@pytest.fixture()
def post_comments_empty_replies_reactions():

    reaction_dtos = [
        ReactionDto(
            id=1, post_id = 1, reacted_by_id = 1,
            comment_id=None, reaction = ReactionType.HAHA.value
        ),
        ReactionDto(
            id=2, post_id = None, reacted_by_id = 1,
            comment_id=1, reaction = ReactionType.WOW.value
        )
    ]
    return reaction_dtos

@pytest.fixture()
def post_empty_replies_details_dto(post_dto,user_dtos,
        post_comments_empty_replies_dtos,
        post_comments_empty_replies_reactions):
    post_details_dto = PostDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=post_comments_empty_replies_dtos,
        reactions_dto=post_comments_empty_replies_reactions
    )
    return post_details_dto

@pytest.fixture()
def post_comment_empty_replies_count_dto():
    
    return [CommentRepliesCountDto(comment_id=1, replies_count=0)]
    
@pytest.fixture()
def comments_empty_replies_reactions_dto():
    return [
        CommentReactionsDto(comment_id=1, reactions=["WOW"], reactions_count=1)
    ]
    

@pytest.fixture()
def post_empty_replies_complete_details_dto(
        post_dto,user_dtos,post_comments_empty_replies_dtos,
        post_comments_empty_replies_reactions,post_reactions_dto,
        post_comments_dto, comments_empty_replies_reactions_dto,
        post_comment_empty_replies_count_dto
    ):
    post_details_dto = PostCompleteDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=post_comments_empty_replies_dtos,
        reactions_dto=post_comments_empty_replies_reactions,
        post_reactions_dto=post_reactions_dto,
        post_comments_dto=post_comments_dto,
        comments_reactions_dto=comments_empty_replies_reactions_dto,
        comment_replies_count_dto=post_comment_empty_replies_count_dto
    )
    return post_details_dto

@pytest.fixture()
def user_posts_empty_replies_details_dto(post_dtos,user_dtos,
        post_comments_empty_replies_dtos,post_comments_empty_replies_reactions):
    post_details_dto = UserPostsDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=post_comments_empty_replies_dtos,
        reactions_dto=post_comments_empty_replies_reactions
    )
    return post_details_dto

@pytest.fixture()
def user_posts_empty_replies_complete_details_dto(
        post_dtos,user_dtos,post_comments_empty_replies_dtos,
        post_comments_empty_replies_reactions, posts_reactions_dto,
        posts_comments_dto, comments_empty_replies_reactions_dto,
        post_comment_empty_replies_count_dto
    ):
    post_details_dto = UserPostsCompleteDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=post_comments_empty_replies_dtos,
        reactions_dto=post_comments_empty_replies_reactions,
        posts_reactions_dto=posts_reactions_dto,
        posts_comments_dto=posts_comments_dto,
        comments_reactions_dto=comments_empty_replies_reactions_dto,
        comment_replies_count_dto=post_comment_empty_replies_count_dto
    )
    return post_details_dto

# task 7

@pytest.fixture()
def user_duplicate_reactions(user_dtos):
    
    user_dtos.append(UserDto(id=3,name="kiranteja",profile_pic="profile_pic3"))
    
    return user_dtos

@pytest.fixture()
def duplicate_reactions():
    reaction_dtos = [
        ReactionDto(
            id=1, post_id = 1, reacted_by_id = 1,
            comment_id=None, reaction = ReactionType.HAHA.value
        ),
        ReactionDto(
            id=2, post_id = 1, reacted_by_id = 2,
            comment_id=None, reaction = ReactionType.HAHA.value
        ),
        ReactionDto(
            id=3, post_id = None, reacted_by_id = 1,
            comment_id=1, reaction = ReactionType.WOW.value
        ),
        ReactionDto(
            id=4, post_id = None, reacted_by_id = 2,
            comment_id=1, reaction = ReactionType.WOW.value
        ),
        ReactionDto(
            id=5, post_id = None, reacted_by_id = 3,
            comment_id=1, reaction = ReactionType.ANGRY.value
        ),
        ReactionDto(
            id=6, post_id = None, reacted_by_id = 1,
            comment_id=2, reaction = ReactionType.ANGRY.value
        ),
        ReactionDto(
            id=7, post_id = None, reacted_by_id = 2,
            comment_id=2, reaction = ReactionType.ANGRY.value
        )
    ]
    return reaction_dtos

@pytest.fixture()
def post_duplicate_reactions_details_dto(post_dto,
        user_duplicate_reactions,comment_dtos,duplicate_reactions):
    post_details_dto = PostDetailsDto(
        post_dto=post_dto,
        users_dto=user_duplicate_reactions,
        comments_dto=comment_dtos,
        reactions_dto=duplicate_reactions
    )
    return post_details_dto

@pytest.fixture()
def post_duplicate_reactions_dto():
    post_reactions_dto = PostReactionsDto(
        post_id=1,reactions=["HAHA"],reactions_count=2
    )
    return post_reactions_dto

@pytest.fixture()
def posts_duplicate_reactions_dto():
    post_reactions_dto = [PostReactionsDto(
        post_id=1,reactions=["HAHA"],reactions_count=2
    )]
    return post_reactions_dto

@pytest.fixture()
def comments_duplicate_reactions_dto():
    return [
        CommentReactionsDto(comment_id=1, reactions=["ANGRY","WOW"], reactions_count=3),
        CommentReactionsDto(comment_id=2, reactions=["ANGRY"], reactions_count=2)
    ]

@pytest.fixture()
def post_duplicate_reactions_complete_details_dto(
        post_dto,user_duplicate_reactions,comment_dtos, duplicate_reactions,
        post_duplicate_reactions_dto, post_comments_dto,
        comments_duplicate_reactions_dto, comment_replies_count_dto
    ):
    post_details_dto = PostCompleteDetailsDto(
        post_dto=post_dto,
        users_dto=user_duplicate_reactions,
        comments_dto=comment_dtos,
        reactions_dto=duplicate_reactions,
        post_reactions_dto=post_duplicate_reactions_dto,
        post_comments_dto=post_comments_dto,
        comments_reactions_dto=comments_duplicate_reactions_dto,
        comment_replies_count_dto=comment_replies_count_dto
    )
    return post_details_dto

@pytest.fixture()
def user_posts_duplicate_reactionsdetails_dto(post_dtos,
        user_duplicate_reactions, comment_dtos,duplicate_reactions):
    post_details_dto = UserPostsDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_duplicate_reactions,
        comments_dto=comment_dtos,
        reactions_dto=duplicate_reactions
    )
    return post_details_dto

@pytest.fixture()
def user_posts_duplicate_reactions_complete_details_dto(
        post_dtos,user_duplicate_reactions,comment_dtos,duplicate_reactions,
        posts_duplicate_reactions_dto, posts_comments_dto,
        comments_duplicate_reactions_dto, comment_replies_count_dto):
    post_details_dto = UserPostsCompleteDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_duplicate_reactions,
        comments_dto=comment_dtos,
        reactions_dto=duplicate_reactions,
        posts_reactions_dto=posts_duplicate_reactions_dto,
        posts_comments_dto=posts_comments_dto,
        comments_reactions_dto=comments_duplicate_reactions_dto,
        comment_replies_count_dto=comment_replies_count_dto
    )
    return post_details_dto


@pytest.fixture()
def get_post_response():
    get_post_response = {
        'post_content': 'My Post Content',
        'post_id': 1,
        'posted_at': '22-04-2019,00:00:00.000000',
        'posted_by': {
            'name': 'raviteja',
            'profile_pic': 'profile_pic1',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'hii',
                'comment_id': 1,
                'commented_at': '22-04-2019,00:00:00.000000',
                'commenter': {
                    'name': 'suryateja',
                    'profile_pic': 'profile_pic2',
                    'user_id': 2
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'WOW'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'hii ra',
                        'comment_id': 2,
                        'commented_at': '22-04-2019,00:00:00.000000',
                        'commenter': {
                            'name': 'suryateja',
                            'profile_pic': 'profile_pic2',
                            'user_id': 2
                        },
                        'reactions' : {
                            'count': 1,
                            'type': ['ANGRY']
                        }
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }
    return get_post_response


@pytest.fixture()
def get_user_posts_response():
    get_user_posts_response = [{
        'post_content': 'My Post Content',
        'post_id': 1,
        'posted_at': '22-04-2019,00:00:00.000000',
        'posted_by': {
            'name': 'raviteja',
            'profile_pic': 'profile_pic1',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'hii',
                'comment_id': 1,
                'commented_at': '22-04-2019,00:00:00.000000',
                'commenter': {
                    'name': 'suryateja',
                    'profile_pic': 'profile_pic2',
                    'user_id': 2
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'WOW'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'hii ra',
                        'comment_id': 2,
                        'commented_at': '22-04-2019,00:00:00.000000',
                        'commenter': {
                            'name': 'suryateja',
                            'profile_pic': 'profile_pic2',
                            'user_id': 2
                        },
                        'reactions' : {
                            'count': 1,
                            'type': ["ANGRY"]
                        }
                    }
                ],
                'replies_count': 2
            }

        ],
        "comments_count": 1
    }]
    return get_user_posts_response

# Apart from get_post and get_user_posts

@pytest.fixture()
def replies_dtos():
    replies_dtos = [
        CommentDto(
            id=3,
            commented_by_id=1,
            post_id=None,
            parent_comment_id=2,
            comment_content='hii ra',
            commented_at=datetime(2019, 4, 22, 0, 0)
        )
    ]
    return replies_dtos

@pytest.fixture()
def replies_users_dtos():
    replies_users_dtos = [
        UserDto(id=2,name="suryateja",profile_pic="profile_pic2")
    ]
    return replies_users_dtos

@pytest.fixture()
def get_replies_for_comment():
    replies_response = [{
        'comment_content': 'hii ra',
        'comment_id': 3,
        'commented_at': '22-04-2019,00:00:00.000000',
        'commenter': {
            'name': 'suryateja',
            'profile_pic': 'profile_pic2',
            'user_id': 2
        }
    }]
    return replies_response

# testcase -2

@pytest.fixture()
def user_posts_details_dto(post_dtos,user_dtos,comment_dtos,reaction_dtos):
    post_details_dto = UserPostsDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=reaction_dtos
    )
    return post_details_dto

@pytest.fixture()
def user_posts_complete_details_dto(
        post_dtos,user_dtos,comment_dtos,reaction_dtos,posts_reactions_dto,
        posts_comments_dto, comments_reactions_dto, comment_replies_count_dto
    ):
    post_details_dto = UserPostsCompleteDetailsDto(
        posts_dto=post_dtos,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=reaction_dtos,
        posts_reactions_dto=posts_reactions_dto,
        posts_comments_dto=posts_comments_dto,
        comments_reactions_dto=comments_reactions_dto,
        comment_replies_count_dto=comment_replies_count_dto
    )
    return post_details_dto






