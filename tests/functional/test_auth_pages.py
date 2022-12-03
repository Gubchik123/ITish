def test_login_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'User login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/auth/login")

    assert response.status_code == 200
    assert b"Login" in response.data


def test_login_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'User login' page is posted to (POST)
    THEN check that the page is ready for POST request
    """
    assert test_client.post("/auth/login").status_code == 200


def test_registration_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'User signup' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/auth/registration")

    assert response.status_code == 200
    assert b"Registration" in response.data


def test_registration_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'User signup' page is posted to (POST)
    THEN check that the page is ready for POST request
    """
    assert test_client.post("/auth/registration").status_code == 200


def test_admin_login_page(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'User signup' page is requested (GET)
    THEN check the response for redirecting to the login page
    """
    assert test_client.get("/auth/login-admin").status_code == 302
    assert test_client.post("/auth/login-admin").status_code == 302
