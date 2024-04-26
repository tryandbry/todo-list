from flask import Flask
from config import Config
from db import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from lists import bp as lists_bp
    app.register_blueprint(lists_bp, url_prefix='/lists')

    @app.route('/health')
    def health():
        return 'OK'

    return app
