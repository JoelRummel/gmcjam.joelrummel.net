import os

from flask import Flask
from flask_mongoengine import MongoEngine


def cround(*args):
    is_flat = float(args[0]) % 1 == 0
    return (int(args[0]) if is_flat else args[0])


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'  # TODO: Randomly generate this in prod
    )
    app.config['MONGODB_SETTINGS'] = {
        "db": "gmcjam43",
    }
    db = MongoEngine()
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from gmcjam.views import show_reviews_bp, add_review_bp
    app.register_blueprint(show_reviews_bp)
    app.register_blueprint(add_review_bp)

    app.add_template_filter(cround)

    return app
