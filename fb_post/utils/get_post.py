from collections import defaultdict
from django.db.models import Prefetch
from fb_post.models import Comment, Post
from fb_post.constants.date_time import get_date_time_format
from .validations import is_valid_post
from typing import *

def get_post(post_id) -> Dict[str, Any]:

    is_valid_post(post_id)
    query_set = Comment.objects\
        .select_related('commented_by')\
        .prefetch_related('reaction_set')
    post_obj: int = Post.objects\
        .filter(id=post_id)\
        .select_related('posted_by')\
        .prefetch_related(
            'reaction_set',
            Prefetch('comment_set', queryset=query_set, to_attr='comments')
        ).first()
    return get_post_details(post_obj)


def get_post_details(post_obj) -> Dict[str, Any]:

    comments_details_list: List[Dict[str, Any]] = get_comments_details_list_for_post(post_obj)

    post_dict: Dict[str, Any] = {
        "post_id": post_obj.id,
        "posted_by": get_user_details(post_obj.posted_by),
        "posted_at": get_date_time_format(post_obj.posted_at),
        "post_content": post_obj.content,
        "reactions": get_reaction_metric_details(
            post_obj.reaction_set.all()
        ),
        "comments": comments_details_list,
        "comments_count": len(comments_details_list)
    }
    return post_dict


def get_comments_details_list_for_post(post_obj) -> Dict[str, Any]:

    comments_list = get_comments_list_for_post(post_obj)
    comment_replies_map = get_comments_dict_for_post(post_obj)
    comments_details_list = []
    for comment in comments_list:
        comments_details_list.append(
            get_comment_details_with_replies(
                comment, comment_replies_map[comment.id])
        )
    return comments_details_list


def get_comments_list_for_post(post_obj):

    comments_list = []
    for comment in post_obj.comments:
        is_comment = not comment.parent_comment_id
        if is_comment:
            comments_list.append(comment)
    return comments_list


def get_comments_dict_for_post(post_obj):

    comments_dict = defaultdict(list)
    for comment in post_obj.comments:
        is_reply = comment.parent_comment_id
        if is_reply:
            comments_dict[comment.parent_comment_id].append(comment)
    return comments_dict


def get_comment_details_with_replies(comment, replies_list):

    comment_dict = get_comment_details(comment)
    extra_comment_dict = {
        "reactions": get_reaction_metric_details(comment.reaction_set.all()),
        "replies_count": len(replies_list),
        "replies": get_replies_details_list(replies_list)
    }
    comment_dict.update(extra_comment_dict)

    return comment_dict


def get_replies_details_list(replies_list):

    replies_details_list = [
        get_reply_details(reply) for reply in replies_list
    ]

    return replies_details_list


def get_reply_details(reply):

    reply_dict = get_comment_details(reply)
    reactions = get_reaction_metric_details(reply.reaction_set.all())
    reply_dict["reactions"] = reactions
    return reply_dict


def get_comment_details(comment):

    comment_details = {
        "comment_id": comment.id,
        "commenter": get_user_details(comment.commented_by),
        "commented_at": get_date_time_format(comment.commented_at),
        "comment_content": comment.content
    }
    return comment_details


def get_reaction_metric_details(reactions_list):

    reaction_dict = {
        "count": len(reactions_list),
        "type": get_unique_reactions_list(reactions_list)
    }
    return reaction_dict


def get_unique_reactions_list(reactions_list):

    post_reactions_set = {
        reaction.reaction for reaction in reactions_list
    }
    post_reactions_list = list(post_reactions_set)
    return sorted(post_reactions_list)


def get_user_details(user_obj):

    user_dict = {
        "user_id": user_obj.id,
        "name": user_obj.name,
        "profile_pic": user_obj.profile_pic
    }
    return user_dict
