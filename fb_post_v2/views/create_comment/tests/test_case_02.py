"""
# TODO: Update test case description
"""
from fb_post_v2.models import Comment
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_v2.utils.custom_test_utils_2 import CustomTestUtils
from fb_post_v2.factories import PostFactory

REQUEST_BODY = """
{
    "content": "string"
}
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


class TestCase01CreateCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreateCommentAPITestCase, self).setupUser(
            username=username, password=password
        )

        PostFactory.reset_sequence(0)
        PostFactory()
        # self.create_user()
        # self.create_posts()

    def test_case(self):
        response = self.default_test_case()
        import json

        response_content = json.loads(response.content)

        comment_id = response_content['comment_id']

        comment = Comment.objects.get(id=comment_id)

        self.assert_match_snapshot(
            name='user_id',
            value=comment.commented_by_id
        )

        self.assert_match_snapshot(
            name='post_id',
            value=comment.post_id
        )
        self.assert_match_snapshot(
            name='comment_text',
            value=comment.content
        )
