# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ReplyToCommentAPITestCase::test_case status'] = 201

snapshots['TestCase01ReplyToCommentAPITestCase::test_case body'] = {
    'reply_id': 2
}

snapshots['TestCase01ReplyToCommentAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '15',
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

snapshots['TestCase01ReplyToCommentAPITestCase::test_case reply comment'] = 'reply content'

snapshots['TestCase01ReplyToCommentAPITestCase::test_case parent post'] = 1
