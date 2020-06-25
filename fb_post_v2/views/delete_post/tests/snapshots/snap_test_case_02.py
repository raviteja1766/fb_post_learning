# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01DeletePostAPITestCase::test_case status'] = 403

snapshots['TestCase01DeletePostAPITestCase::test_case body'] = {
    'http_status_code': 403,
    'res_status': 'USER_CANNOT_DELETE_POST_EXCEPTION',
    'response': 'Please send Original Post Author'
}

snapshots['TestCase01DeletePostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '124',
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