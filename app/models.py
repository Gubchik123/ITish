import re
import datetime

from flask_login import UserMixin

from .db import db


class User(db.Model, UserMixin):
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


def get_correct_str_from_(s: str):
    return re.sub(pattern=r"[^\w+]", repl="-", string=s)


post_tags = db.Table(
    "post_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")),
)


class General:
    def generate_correct_url(self):
        self.url = get_correct_str_from_(self.title)

    def __repr__(self) -> str:
        return f"<{self.title}>"


class Post(General, db.Model):
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
        super(Post, self).__init__(*args, **kwargs)
        self.generate_correct_url()


class Tag(General, db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    url = db.Column(db.String(30), nullable=False, unique=True)

    def __init__(self, *args, **kwargs) -> None:
        super(Tag, self).__init__(*args, **kwargs)
        self.generate_correct_url()


class Comment(db.Model):
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
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    post_id = db.Column(
        db.Integer, db.ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )
