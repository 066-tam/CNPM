from flask import Flask
from flask_migrate import Migrate
from controllers import register_routes
from error_handler import register_error_handlers
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)  # Thêm migrate

    register_routes(app)
    register_error_handlers(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
