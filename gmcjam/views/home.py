import flask

bp = flask.Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def landing_page():
    return flask.redirect("/reviews/")
