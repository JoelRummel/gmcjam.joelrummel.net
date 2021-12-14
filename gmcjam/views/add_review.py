import flask
from gmcjam.models.review import Review

bp = flask.Blueprint("addReview", __name__, url_prefix="/addReview")


@bp.route("/", methods=["GET", "POST"])
def add_review():
    if flask.request.method == "POST":
        # Add review to DB
        form = flask.request.form
        new_review = Review()
        new_review.game_name = form["game_name"]
        new_review.authors = form["authors"]
        new_review.slug = form["game_name"] + " by " + form["authors"]
        new_review.player_experience_score = float(
            form["player_experience_score"])
        new_review.mechanical_polish_score = float(
            form["mechanical_polish_score"])
        new_review.overall_gameplay_comments = form["overall_gameplay_comments"]
        new_review.theme_inclusion_score = float(form["theme_inclusion_score"])
        new_review.theme_inclusion_comments = form["theme_inclusion_comments"]
        new_review.general_presentation_score = float(
            form["general_presentation_score"])
        new_review.quality_graphics_score = float(
            form["quality_graphics_score"])
        new_review.quality_audio_score = float(form["quality_audio_score"])
        new_review.overall_presentation_comments = form["overall_presentation_comments"]
        new_review.total_score = float(form["player_experience_score"]) + float(form["mechanical_polish_score"]) + \
            float(form["theme_inclusion_score"]) + float(form["general_presentation_score"]) + \
            float(form["quality_graphics_score"]) + \
            float(form["quality_audio_score"])
        new_review.final_comments = form["final_comments"]
        new_review.play_time = form["play_time"]
        new_review.save()

    context = {
        "review_added": False
    }

    return flask.render_template("add_review.html", **context)
