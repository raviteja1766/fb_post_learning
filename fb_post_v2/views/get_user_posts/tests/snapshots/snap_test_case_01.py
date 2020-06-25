# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserPostsAPITestCase::test_case status'] = 201

snapshots['TestCase01GetUserPostsAPITestCase::test_case body'] = [
    {
        'comments': [
            {
                'comment_content': 'comment_1',
                'comment_id': 1,
                'commented_at': '03-04-2012 00:00:00.000000',
                'commenter': {
                    'name': 'user_2',
                    'profile_pic': 'profile_pic_2',
                    'user_id': 2
                },
                'reactions': {
                    'count': 3,
                    'type': [
                        'LIT',
                        'LOVE',
                        'WOW'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'comment_18',
                        'comment_id': 18,
                        'commented_at': '03-04-2012 00:00:00.000000',
                        'commenter': {
                            'name': '',
                            'profile_pic': '',
                            'user_id': 1
                        },
                        'reactions': {
                            'count': 3,
                            'type': [
                                'HAHA',
                                'THUMBS-DOWN',
                                'THUMBS-UP'
                            ]
                        }
                    }
                ],
                'replies_count': 1
            },
            {
                'comment_content': 'comment_2',
                'comment_id': 2,
                'commented_at': '03-04-2012 00:00:00.000000',
                'commenter': {
                    'name': 'user_3',
                    'profile_pic': 'profile_pic_3',
                    'user_id': 3
                },
                'reactions': {
                    'count': 3,
                    'type': [
                        'HAHA',
                        'THUMBS-DOWN',
                        'THUMBS-UP'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'comment_19',
                        'comment_id': 19,
                        'commented_at': '03-04-2012 00:00:00.000000',
                        'commenter': {
                            'name': 'user_2',
                            'profile_pic': 'profile_pic_2',
                            'user_id': 2
                        },
                        'reactions': {
                            'count': 3,
                            'type': [
                                'ANGRY',
                                'SAD',
                                'WOW'
                            ]
                        }
                    },
                    {
                        'comment_content': 'comment_20',
                        'comment_id': 20,
                        'commented_at': '03-04-2012 00:00:00.000000',
                        'commenter': {
                            'name': 'user_3',
                            'profile_pic': 'profile_pic_3',
                            'user_id': 3
                        },
                        'reactions': {
                            'count': 3,
                            'type': [
                                'HAHA',
                                'LIT',
                                'LOVE'
                            ]
                        }
                    }
                ],
                'replies_count': 2
            }
        ],
        'comments_count': 2,
        'post_content': 'post_1',
        'post_id': 1,
        'posted_at': '03-04-2012 00:00:00.000000',
        'posted_by': {
            'name': '',
            'profile_pic': '',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'WOW'
            ]
        }
    },
    {
        'comments': [
            {
                'comment_content': 'comment_3',
                'comment_id': 3,
                'commented_at': '03-04-2012 00:00:00.000000',
                'commenter': {
                    'name': 'user_4',
                    'profile_pic': 'profile_pic_4',
                    'user_id': 4
                },
                'reactions': {
                    'count': 3,
                    'type': [
                        'ANGRY',
                        'SAD',
                        'WOW'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'comment_21',
                        'comment_id': 21,
                        'commented_at': '03-04-2012 00:00:00.000000',
                        'commenter': {
                            'name': 'user_4',
                            'profile_pic': 'profile_pic_4',
                            'user_id': 4
                        },
                        'reactions': {
                            'count': 3,
                            'type': [
                                'ANGRY',
                                'THUMBS-DOWN',
                                'THUMBS-UP'
                            ]
                        }
                    }
                ],
                'replies_count': 1
            }
        ],
        'comments_count': 1,
        'post_content': 'post_2',
        'post_id': 2,
        'posted_at': '03-04-2012 00:00:00.000000',
        'posted_by': {
            'name': '',
            'profile_pic': '',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'LIT'
            ]
        }
    }
]

snapshots['TestCase01GetUserPostsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '2227',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
