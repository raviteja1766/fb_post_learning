# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetRepliesToCommentAPITestCase::test_case status'] = 201

snapshots['TestCase01GetRepliesToCommentAPITestCase::test_case body'] = [
    {
        'comment_content': 'comment_1',
        'comment_id': 2,
        'commented_at': '03-04-2012 00:00:00.000000',
        'commenter': {
            'name': 'user_2',
            'profile_pic': 'profile_pic_2',
            'user_id': 2
        }
    },
    {
        'comment_content': 'comment_2',
        'comment_id': 3,
        'commented_at': '03-04-2012 00:00:00.000000',
        'commenter': {
            'name': 'user_3',
            'profile_pic': 'profile_pic_3',
            'user_id': 3
        }
    },
    {
        'comment_content': 'comment_3',
        'comment_id': 4,
        'commented_at': '03-04-2012 00:00:00.000000',
        'commenter': {
            'name': 'user_4',
            'profile_pic': 'profile_pic_4',
            'user_id': 4
        }
    }
]

snapshots['TestCase01GetRepliesToCommentAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '528',
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
