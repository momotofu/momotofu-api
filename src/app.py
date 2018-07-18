from flask import Flask
from .config import Config as default_config
from .utils.utils import get_session

def create_app(config=None):
    """
    Configure app object blueprints and global variables.
    """

    app = configure_app(Flask(__name__), config)

    # setup flask blueprints
    configure_blueprints(app)

    return app


def configure_app(app, config_object=None):
    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(default_config)

    return app


def configure_blueprints(app):
    from .api.blog import blog_bp

    for blueprint in [blog_bp]:
        app.register_blueprint(blueprint)

    return app
