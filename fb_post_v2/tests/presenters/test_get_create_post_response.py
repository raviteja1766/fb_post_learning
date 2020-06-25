from fb_post_v2.presenters.presenter_implementation\
    import PresenterImplementation

def test_get_create_post_response_given_post_id_return_response_dict():
    
    # Arrange
    post_id = 1
    presenter = PresenterImplementation()
    expected_dict = {"post_id": 1}
    
    # Act
    response_dict = presenter.get_create_post_response(post_id=post_id)
    
    # Assert
    assert response_dict == expected_dict