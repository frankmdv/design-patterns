from flask import Flask


def init_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Register blueprints
    with app.app_context():
        from app.public import bp as public_bp

        app.register_blueprint(public_bp)

    return app
