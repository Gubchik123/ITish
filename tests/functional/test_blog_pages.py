def test_valid_js_file_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the view for getting js file is requested (GET)
    THEN check the file was found
    """
    assert test_client.get("/blog/js-file/scrolling.js").status_code == 200


def test_invalid_js_file_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the view for getting js file is requested (GET)
    THEN check the file was not found
    """
    assert test_client.get("/blog/js-file/does_not_exist_file.js").status_code == 404


def test_js_file_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the '/Blog' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/blog/js-file/some_file.js")

    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data


def test_blog_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the '/Blog' page is requested (GET)
    THEN check the page with all posts is returned
    """
    response = test_client.get("/blog/")

    assert response.status_code == 200
    assert b"All posts" in response.data


def test_blog_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the '/Blog' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/blog/")

    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data
    assert b"All posts" not in response.data


def test_all_posts_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the '/Blog' page with tab = 'posts' is requested (GET)
    THEN check the page with all posts is returned
    """
    response = test_client.get("/blog/?tab=posts")

    assert response.status_code == 200
    assert b"All posts" in response.data


def test_all_tags_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the '/Blog' page with tab = 'tags' is requested (GET)
    THEN check the page with all tags is returned
    """
    response = test_client.get("/blog/?tab=tags")

    assert response.status_code == 200
    assert b"All tags" in response.data


def test_posts_by_tag_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'Posts with tag ...' page is requested (GET)
    THEN check the tag was not found
    """
    response = test_client.get("/blog/tag/does-not-exist")

    assert response.status_code == 404
    assert b"Not Found" in response.data


def test_posts_by_tag_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'Posts with tag ...' page is requested (GET)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/blog/tag/does-not-exist")

    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data


def test_post_page_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'Post' page is requested (GET)
    THEN check the post was not found
    """
    response = test_client.get("/blog/post/does-not-exist")

    assert response.status_code == 404
    assert b"Not Found" in response.data


def test_post_page_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the 'Post' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/blog/post/does-not-exist")

    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data


def test_login_required_views_get(test_client):
    """
    GIVEN a Flask test client
    WHEN the login required pages is requested (GET)
    THEN check the response for redirecting to the login page
    """
    post_url = "/post/does-not-exist"

    assert test_client.get("/blog/create-post").status_code == 302
    assert test_client.get(f"/blog{post_url}/delete").status_code == 302
    assert test_client.get(f"/blog{post_url}/delete-comment/1").status_code == 302
    assert test_client.get(f"/blog{post_url}/edit").status_code == 302


def test_login_required_views_post(test_client):
    """
    GIVEN a Flask test client
    WHEN the login required pages is posted to (POST)
    THEN check the response for redirecting to the login page
    """
    post_url = "/post/does-not-exist"

    assert test_client.post(f"/blog{post_url}/like").status_code == 302
    assert test_client.post(f"/blog{post_url}/comment").status_code == 302
    assert test_client.post(f"/blog{post_url}/edit").status_code == 302
