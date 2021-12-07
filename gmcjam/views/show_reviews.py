import flask
from gmcjam.models.review import Review

bp = flask.Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("/")
def all_reviews():
    reviews = Review.objects().filter()

    context = {
        "reviews": reviews,
        "num_reviews": len(reviews)
    }

    return flask.render_template("all_reviews.html", **context)


@bp.route("/<string:review_slug>")
def one_review(review_slug):
    review = Review.objects(slug=review_slug).get_or_404()

    context = {
        "review": review
    }

    return flask.render_template("single_review.html", **context)
