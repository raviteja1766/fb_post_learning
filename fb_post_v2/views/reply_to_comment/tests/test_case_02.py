"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_v2.factories import *
from freezegun import freeze_time
from fb_post_v2.models import Comment

REQUEST_BODY = """
{
    "content": "reply content"
}
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


class TestCase01ReplyToCommentAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    @freeze_time("2012-03-04")
    def setupUser(self, username, password):
        super(TestCase01ReplyToCommentAPITestCase, self).setupUser(
            username=username, password=password
        )
        PostFactory.reset_sequence(0)
        UserFactory.reset_sequence(0)
        CommentFactory.reset_sequence(0)
        user = UserFactory()
        post = PostFactory()
        CommentFactory(post=post, commented_by=user)



    def test_case(self):
        response = self.default_test_case()
        import json
        reply_id = json.loads(response.content)['reply_id']
        reply_obj = Comment.objects.get(id=reply_id)
        self.assert_match_snapshot(
            name='reply comment',
            value=reply_obj.content
        )
        self.assert_match_snapshot(
            name='parent post',
            value=reply_obj.parent_comment.post_id
        )
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.