# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_posts_reacted_by_user"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/reacted_posts/v1/"

from .test_case_01 import TestCase01GetPostsReactedByUserAPITestCase

__all__ = [
    "TestCase01GetPostsReactedByUserAPITestCase"
]
