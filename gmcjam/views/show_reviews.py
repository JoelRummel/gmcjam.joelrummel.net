import flask
from gmcjam.models.review import Review
import functools

bp = flask.Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("/")
def all_reviews():
    reviews = Review.objects().filter()
    print(type(reviews))

    sort = flask.request.args.get("s") or "recent"
    if sort == "score":
        reviews = sorted(
            reviews, key=lambda review: review["total_score"], reverse=True)
    if sort == "name":
        reviews = sorted(reviews, key=lambda review: review["game_name"])
    if sort == "recent":
        pass  # reviews = sorted(reviews, reverse=True)

    context = {
        "reviews": reviews,
        "num_reviews": len(reviews),
        "sort": sort
    }

    return flask.render_template("all_reviews.html", **context)


@bp.route("/<string:review_slug>")
def one_review(review_slug):
    review = Review.objects(slug=review_slug).get_or_404()

    context = {
        "review": review
    }

    return flask.render_template("single_review.html", **context)
