def test_redirecting_to_login_page(test_client):
    """
    GIVEN a Flask test client
    WHEN the page which is login required is requested (GET)
    THEN check the response for redirecting to the login page
    """
    assert test_client.get("/blog/create-post").status_code == 302


def test_404_error_code(test_client):
    """
    GIVEN a Flask test client
    WHEN the page which doesn't exist is requested (GET)
    THEN check the response with '404' error code
    """
    response = test_client.get("/test-url-which-does-not-exist")

    assert response.status_code == 404
    assert b"Not Found" in response.data
