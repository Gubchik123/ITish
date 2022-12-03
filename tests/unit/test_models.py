from app.models import User, Post, Tag, Like, Comment


def test_new_user(new_user: User):
    """
    GIVEN a User model
    WHEN new user is created
    THEN check the user data are defined correctly
    """
    assert new_user.username == "test_username"
    assert new_user.email == "test_email@gmail.com"
    assert new_user.password != "test_password"


def test_new_post(new_post: Post):
    """
    GIVEN a Post model
    WHEN new post is created
    THEN check the post data are defined correctly
    """
    assert new_post.title == "Test title"
    assert new_post.url == "Test-title"
    assert new_post.body == "<h2>Test post content</h2>"
    assert new_post.user_id == 1
    assert new_post.tags == []
    assert new_post.likes.all() == []
    assert new_post.comments.all() == []


def test_new_tag(new_tag: Tag):
    """
    GIVEN a Tag model
    WHEN new tag is created
    THEN check the title and url are defined correctly
    """
    assert new_tag.title == "test tag"
    assert new_tag.url == "test-tag"


def test_new_like(new_like: Like):
    """
    GIVEN a Like model
    WHEN new like is created
    THEN check the user id, post id and created time are defined correctly
    """
    assert new_like.user_id == 1
    assert new_like.post_id == 1


def test_new_comment(new_comment: Comment):
    """
    GIVEN a Comment model
    WHEN new comment is created
    THEN check the user id, post id and created time are defined correctly
    """
    assert new_comment.user_id == 1
    assert new_comment.post_id == 1
    assert new_comment.body == "Test comment"
