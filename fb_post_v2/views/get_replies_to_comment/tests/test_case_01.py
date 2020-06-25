"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from freezegun import freeze_time
from fb_post_v2.factories import *

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetRepliesToCommentAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    @freeze_time("2012-03-04")
    def setupUser(self, username, password):
        super(TestCase01GetRepliesToCommentAPITestCase, self).setupUser(
            username=username, password=password
        )
        UserFactory.reset_sequence(2)
        PostFactory.reset_sequence(0)
        CommentFactory.reset_sequence(0)
        users = UserFactory.create_batch(size=3)
        post = PostFactory()
        CommentFactory.commented_by.reset()
        comment = CommentFactory(post=post)
        for user in users:
            ReplyFactory(parent_comment=comment, commented_by=user)

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
