import flask
import flask_login as flog

from ..app import app
from ..models import Post, Tag
from ..extensions import db
from .forms import PostCreateForm, PostEditForm


def get_js_file(filename: str):
    return flask.send_from_directory(
        app.config["UPLOAD_FOLDER"],
        f"js/{filename}" if ".js" in filename else f"js/{filename}.js",
        as_attachment=True,
        mimetype="text/javascript",
    )


def get_blog_page():
    tab = flask.request.args.get("tab")
    tab = tab if tab else "posts"

    return (
        _get_all_posts()
        if tab == "posts"
        else (_get_all_tags() if tab == "tags" else flask.abort(404))
    )


def _get_all_posts():
    q = flask.request.args.get("q", "")

    posts = (
        Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).order_by(
            Post.created.desc()
        ).all()
        if q
        else Post.query.order_by(Post.created.desc()).all()
    )

    print(posts)

    return flask.render_template("blog/all_posts.html", posts=posts)


def _get_all_tags():
    return flask.render_template(
        "blog/all_tags.html", tags=Tag.query.order_by(Tag.url).all()
    )


def _add_post_in_db_from_(form: PostCreateForm):
    db.session.add(
        Post(
            title=form.post_title.data,
            body=form.post_body.data,
            user_id=flog.current_user.id,
        )
    )
    db.session.commit()


@flog.login_required
def create_post():
    form = PostCreateForm()

    if form.validate_on_submit():
        _add_post_in_db_from_(form)
        flask.flash("Post has successfully added", category="success")

    return flask.render_template("blog/create_post.html", form=form)


def get_all_posts_with_(tag: str):
    pass


def get_post_by_(post_url: str):
    post = Post.query.filter(Post.url == post_url).first_or_404()
    return flask.render_template("blog/post.html", post=post)


@flog.login_required
def like_post_with_(post_url: str):
    pass


@flog.login_required
def comment_post_with_(post_url: str):
    pass


@flog.login_required
def edit_post_with_(post_url: str):
    form = PostEditForm()
    post = Post.query.filter(Post.url == post_url).first_or_404()

    if form.validate_on_submit():
        post.title = form.post_title.data
        post.body = form.post_body.data
        db.session.commit()

        flask.flash("Post has successfully edited", category="success")
        return flask.redirect(flask.url_for("blog.get_post_by_", post_url=post_url))

    return flask.render_template("blog/edit_post.html", form=form, post=post)
