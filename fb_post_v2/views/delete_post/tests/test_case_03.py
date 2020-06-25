"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_v2.factories import PostFactory, UserFactory
from fb_post_v2.models import Post

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01DeletePostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01DeletePostAPITestCase, self).setupUser(
            username=username, password=password
        )
        PostFactory.reset_sequence(0)
        PostFactory()

    def test_case(self):

        self.default_test_case()

        boolean = Post.objects.filter(id=1).exists()

        self.assert_match_snapshot(
            name='post_id',
            value=boolean
        )
