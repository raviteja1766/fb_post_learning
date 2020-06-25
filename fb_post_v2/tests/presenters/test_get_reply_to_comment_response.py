from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation

def test_get_reply_to_comment_response_given_post_id_return_response_dict():
    
    # Arrange
    reply_id = 1
    presenter = PresenterImplementation()
    expected_dict = {"reply_id": 1}
    
    # Act
    response_dict = presenter.get_reply_to_comment_response(reply_id=reply_id)
    
    # Assert
    assert response_dict == expected_dict