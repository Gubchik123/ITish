import flask


def get_home_page():
    return flask.render_template("index.html")


def get_FAQs_page():
    return flask.render_template("FAQs.html")


def get_about_page():
    return flask.render_template("about.html")


def abort_to_login_page():
    return flask.redirect(flask.url_for("auth.log_in_user"))


def get_error_page(error):
    return flask.render_template("error.html", error=error), error.code
