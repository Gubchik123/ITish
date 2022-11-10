import flask


def get_home_page():
    return flask.render_template("index.html")


def get_FAQs_page():
    return flask.render_template("FAQs.html")


def get_about_page():
    return flask.render_template("about.html")


def _get_logout_page_url():
    return flask.request.url_root[:-1] + flask.url_for("auth.log_out_user")


def abort_to_login_page():
    next = flask.request.url if flask.request.url != _get_logout_page_url() else None
    return flask.redirect(flask.url_for("auth.log_in_user", next=next))


def get_error_page(error):
    return flask.render_template("error.html", error=error), error.code
