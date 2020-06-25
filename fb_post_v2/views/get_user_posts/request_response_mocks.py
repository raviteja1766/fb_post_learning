


RESPONSE_200_JSON = """
{
    "total": 1,
    "posts": [
        {
            "post_id": 1,
            "posted_by": {
                "name": "string",
                "profile_pic": "string",
                "user_id": 1
            },
            "posted_at": "string",
            "post_content": "string",
            "reactions": {
                "count": 1,
                "type": [
                    "WOW"
                ]
            },
            "comments": [
                {
                    "comment_id": 1,
                    "commenter": {
                        "name": "string",
                        "profile_pic": "string",
                        "user_id": 1
                    },
                    "commented_at": "string",
                    "comment_content": "string",
                    "reactions": {
                        "count": 1,
                        "type": [
                            "WOW"
                        ]
                    },
                    "replies_count": 1,
                    "replies": [
                        {
                            "comment_id": 1,
                            "commenter": {
                                "name": "string",
                                "profile_pic": "string",
                                "user_id": 1
                            },
                            "commented_at": "string",
                            "comment_content": "string",
                            "reactions": {
                                "count": 1,
                                "type": [
                                    "WOW"
                                ]
                            }
                        }
                    ]
                }
            ],
            "comments_count": 1
        }
    ]
}
"""

