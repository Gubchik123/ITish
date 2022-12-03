def test_user_profile_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'User profile' page is requested (GET)
    THEN check the response for redirecting to the login page
    """
    assert test_client.get("/user/does-not-exist").status_code == 302


def test_user_profile_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'User profile' page is requested (GET)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/user/does-not-exist")

    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data
