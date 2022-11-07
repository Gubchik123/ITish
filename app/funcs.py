import flask


def get_home_page():
    return flask.render_template("index.html")
