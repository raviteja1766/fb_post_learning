"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_v2.utils.custom_test_utils_2 import CustomTestUtils
from fb_post_v2.models import Post

REQUEST_BODY = """
{
    "content": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {
            "oauth": {
                "tokenUrl": "http://auth.ibtspl.com/oauth2/",
                "flow": "password",
                "scopes": ["superuser"],
                "type": "oauth2"
                
            }
        },
        "body": REQUEST_BODY,
    },
}


class TestCase01CreatePostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        response = self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        import json

        response_content = json.loads(response.content)

        post_id = response_content['post_id']

        post = Post.objects.get(id=post_id)

        self.assert_match_snapshot(
            name='user_id',
            value=post.posted_by_id
        )

        self.assert_match_snapshot(
            name='post_id',
            value=post.id
        )

        self.assert_match_snapshot(
            name='post_content',
            value=post.content
        )