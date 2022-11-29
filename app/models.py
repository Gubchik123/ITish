import re
import datetime

from flask_login import UserMixin

from .db import db


class User(db.Model, UserMixin):
    """Model for storing information about users"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(110), nullable=False)
    created = db.Column(db.Date, default=datetime.date.today())
    avatar = db.Column(db.LargeBinary)

    posts = db.relationship(
        "Post",
        backref=db.backref("user", lazy="joined"),
        lazy="dynamic",
        passive_deletes=True,
    )
    comments = db.relationship(
        "Comment",
        backref=db.backref("user", lazy="joined"),
        lazy="dynamic",
        passive_deletes=True,
    )
    likes = db.relationship(
        "Like",
        backref=db.backref("user", lazy="joined"),
        lazy="dynamic",
        passive_deletes=True,
    )


def get_correct_str_from_(s: str) -> str:
    """For getting correct string replacing all spaces with hyphen"""
    return re.sub(pattern=r"[^\w+]", repl="-", string=s)


# Table for many-to-many relationship between posts and tags
post_tags = db.Table(
    "post_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")),
)


class ModelWithUrl:
    """For models with 'url' column for inheritance"""

    def generate_correct_url(self) -> None:
        """For setting correct url"""
        self.url = get_correct_str_from_(self.title)

    def __repr__(self) -> str:
        """For getting 'title' column"""
        return f"<{self.title}>"


class Post(ModelWithUrl, db.Model):
    """Model for storing information about posts"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False, unique=True)
    url = db.Column(db.String(70), nullable=False, unique=True)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    tags = db.relationship(
        "Tag", secondary=post_tags, backref=db.backref("posts", lazy="dynamic")
    )
    comments = db.relationship(
        "Comment",
        backref=db.backref("post", lazy="joined"),
        lazy="dynamic",
        passive_deletes=True,
    )
    likes = db.relationship(
        "Like",
        backref=db.backref("post", lazy="joined"),
        lazy="dynamic",
        passive_deletes=True,
    )

    def __init__(self, *args, **kwargs) -> None:
        """For setting correct url during initializing"""
        super(Post, self).__init__(*args, **kwargs)
        self.generate_correct_url()


class Tag(ModelWithUrl, db.Model):
    """Model for storing information about tags"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    url = db.Column(db.String(30), nullable=False, unique=True)

    def __init__(self, *args, **kwargs) -> None:
        """For setting correct url during initializing"""
        super(Tag, self).__init__(*args, **kwargs)
        self.generate_correct_url()


class Comment(db.Model):
    """Model for storing information about comments"""

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    post_id = db.Column(
        db.Integer, db.ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )


class Like(db.Model):
    """Model for storing information about likes"""

    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    post_id = db.Column(
        db.Integer, db.ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )
