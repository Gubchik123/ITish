def test_home_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'Home' ('/') page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/")

    assert response.status_code == 200
    assert b"Home page" in response.data


def test_home_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'Home' ('/') page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/")

    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data
    assert b"Home page" not in response.data


def test_FAQs_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'FAQs' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/FAQs")

    assert response.status_code == 200
    assert b"FAQs" in response.data


def test_FAQs_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'FAQs' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/FAQs")

    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data
    assert b"FAQs" not in response.data


def test_about_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'About' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/about")

    assert response.status_code == 200
    assert b"About" in response.data


def test_about_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'About' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/about")

    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data
    assert b"About" not in response.data
