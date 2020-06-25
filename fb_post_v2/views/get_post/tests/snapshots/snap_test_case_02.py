# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPostAPITestCase::test_case status'] = 201

snapshots['TestCase01GetPostAPITestCase::test_case body'] = {
    'comments': [
        {
            'comment_content': 'comment_0',
            'comment_id': 1,
            'commented_at': '03-04-2012 00:00:00.000000',
            'commenter': {
                'name': '',
                'profile_pic': '',
                'user_id': 1
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
                    'comment_content': 'comment_3',
                    'comment_id': 4,
                    'commented_at': '03-04-2012 00:00:00.000000',
                    'commenter': {
                        'name': 'user_2',
                        'profile_pic': 'profile_pic_2',
                        'user_id': 4
                    },
                    'reactions': {
                        'count': 3,
                        'type': [
                            'HAHA',
                            'LIT',
                            'LOVE'
                        ]
                    }
                },
                {
                    'comment_content': 'comment_4',
                    'comment_id': 5,
                    'commented_at': '03-04-2012 00:00:00.000000',
                    'commenter': {
                        'name': 'user_3',
                        'profile_pic': 'profile_pic_3',
                        'user_id': 5
                    },
                    'reactions': {
                        'count': 3,
                        'type': [
                            'ANGRY',
                            'THUMBS-DOWN',
                            'THUMBS-UP'
                        ]
                    }
                },
                {
                    'comment_content': 'comment_5',
                    'comment_id': 6,
                    'commented_at': '03-04-2012 00:00:00.000000',
                    'commenter': {
                        'name': 'user_4',
                        'profile_pic': 'profile_pic_4',
                        'user_id': 6
                    },
                    'reactions': {
                        'count': 3,
                        'type': [
                            'LIT',
                            'SAD',
                            'WOW'
                        ]
                    }
                }
            ],
            'replies_count': 3
        },
        {
            'comment_content': 'comment_1',
            'comment_id': 2,
            'commented_at': '03-04-2012 00:00:00.000000',
            'commenter': {
                'name': 'user_0',
                'profile_pic': 'profile_pic_0',
                'user_id': 2
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
                    'comment_content': 'comment_6',
                    'comment_id': 7,
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
                            'LOVE',
                            'THUMBS-UP'
                        ]
                    }
                },
                {
                    'comment_content': 'comment_7',
                    'comment_id': 8,
                    'commented_at': '03-04-2012 00:00:00.000000',
                    'commenter': {
                        'name': 'user_0',
                        'profile_pic': 'profile_pic_0',
                        'user_id': 2
                    },
                    'reactions': {
                        'count': 3,
                        'type': [
                            'ANGRY',
                            'SAD',
                            'THUMBS-DOWN'
                        ]
                    }
                },
                {
                    'comment_content': 'comment_8',
                    'comment_id': 9,
                    'commented_at': '03-04-2012 00:00:00.000000',
                    'commenter': {
                        'name': 'user_1',
                        'profile_pic': 'profile_pic_1',
                        'user_id': 3
                    },
                    'reactions': {
                        'count': 3,
                        'type': [
                            'LIT',
                            'LOVE',
                            'WOW'
                        ]
                    }
                }
            ],
            'replies_count': 3
        },
        {
            'comment_content': 'comment_2',
            'comment_id': 3,
            'commented_at': '03-04-2012 00:00:00.000000',
            'commenter': {
                'name': 'user_1',
                'profile_pic': 'profile_pic_1',
                'user_id': 3
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
                    'comment_content': 'comment_9',
                    'comment_id': 10,
                    'commented_at': '03-04-2012 00:00:00.000000',
                    'commenter': {
                        'name': 'user_2',
                        'profile_pic': 'profile_pic_2',
                        'user_id': 4
                    },
                    'reactions': {
                        'count': 3,
                        'type': [
                            'HAHA',
                            'THUMBS-DOWN',
                            'THUMBS-UP'
                        ]
                    }
                },
                {
                    'comment_content': 'comment_10',
                    'comment_id': 11,
                    'commented_at': '03-04-2012 00:00:00.000000',
                    'commenter': {
                        'name': 'user_3',
                        'profile_pic': 'profile_pic_3',
                        'user_id': 5
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
                    'comment_content': 'comment_11',
                    'comment_id': 12,
                    'commented_at': '03-04-2012 00:00:00.000000',
                    'commenter': {
                        'name': 'user_4',
                        'profile_pic': 'profile_pic_4',
                        'user_id': 6
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
            'replies_count': 3
        }
    ],
    'comments_count': 0,
    'post_content': 'post_0',
    'post_id': 1,
    'posted_at': '03-04-2012 00:00:00.000000',
    'posted_by': {
        'name': 'user_0',
        'profile_pic': 'profile_pic_0',
        'user_id': 2
    },
    'reactions': {
        'count': 0,
        'type': [
        ]
    }
}

snapshots['TestCase01GetPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '3184',
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
