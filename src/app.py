from flask import Flask
from .utils.utils import get_session

def create_app(config='dev'):
    """
    Configure app object blueprints and global variables.
    """
    if config == 'dev':
        from .conf.config import DevelopmentConfig as dev_config
        app = configure_app(Flask(__name__), dev_config)
    else:
        from .conf.config import ProdConfig
        app = configure_app(Flask(__name__), ProdConfig)

    # setup flask blueprints
    configure_blueprints(app)

    return app


def configure_app(app, config_object=None):
    app.config.from_object(config_object)
    return app


def configure_blueprints(app):
    from .api.blog import blog_bp

    for blueprint in [blog_bp]:
        app.register_blueprint(blueprint)

    return app
