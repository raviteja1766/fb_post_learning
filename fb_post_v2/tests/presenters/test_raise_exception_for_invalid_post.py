from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation
import pytest
from fb_post_v2.constants.exception_messages import INVALID_POST_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound

def test_raise_exception_for_invalid_post_raises_exception():
    
    # Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_POST_EXCEPTION[0]
    
    # Act
    with pytest.raises(NotFound) as e:
        presenter.raise_exception_for_invalid_post()

    # Assert
    assert str(e.value) == exception_messages