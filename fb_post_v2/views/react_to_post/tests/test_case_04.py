"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from freezegun import freeze_time
from fb_post_v2.factories import PostFactory, PostReactionFactory
from fb_post_v2.models import Reaction

REQUEST_BODY = """
{
    "reaction_type": "WOW"
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


class TestCase01ReactToPostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    @freeze_time("2012-03-04")
    def setupUser(self, username, password):
        super(TestCase01ReactToPostAPITestCase, self).setupUser(
            username=username, password=password
        )
        PostFactory.reset_sequence(0)
        PostReactionFactory.reset_sequence(0)
        post = PostFactory()
        PostReactionFactory(
            post=post, reacted_by=self.foo_user, reaction="HAHA"
        )

    def test_case(self):
        self.default_test_case()

        reaction_obj = Reaction.objects.get(post_id=1, reacted_by_id=1)

        self.assert_match_snapshot(
            name='reaction_type',
            value=reaction_obj.reaction
        )

        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.