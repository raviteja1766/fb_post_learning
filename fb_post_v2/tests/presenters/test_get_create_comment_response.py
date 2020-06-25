from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation

def test_get_create_comment_response_given_post_id_return_response_dict():
    
    # Arrange
    comment_id = 1
    presenter = PresenterImplementation()
    expected_dict = {"comment_id": 1}
    
    # Act
    response_dict = presenter.get_create_comment_response(
        comment_id=comment_id)
    
    # Assert
    assert response_dict == expected_dict