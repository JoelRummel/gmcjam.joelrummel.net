import flask
from gmcjam.models.review import Review

bp = flask.Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("/")
def all_reviews():
    reviews = Review.objects()

    context = {
        "reviews": reviews.filter()
    }

    return flask.render_template("all_reviews.html", **context)


@bp.route("/add")
def add_review():
    new_review = Review()
    new_review.game_name = "Cool Game"
    new_review.authors = "Nobody"
    new_review.slug = "Cool Game by Nobody"
    new_review.player_experience_score = 8.5
    new_review.mechanical_polish_score = 2
    new_review.overall_gameplay_comments = "It was pretty good I guess"
    new_review.theme_inclusion_score = 3
    new_review.theme_inclusion_comments = "Bro where even was the theme"
    new_review.general_presentation_score = 1
    new_review.quality_graphics_score = 1.5
    new_review.quality_audio_score = 1.5
    new_review.overall_presentation_comments = "Ugly as shit man"
    new_review.total_score = 17.5

    new_review.save()
    return flask.render_template_string("<p>Review created successfully</p>")


@bp.route("/<string:review_slug>")
def one_review(review_slug):
    review = Review.objects(slug=review_slug).get_or_404()

    context = {
        "review": review
    }

    return flask.render_template("single_review.html", **context)
