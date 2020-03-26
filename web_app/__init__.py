
# web_app/__init__.py

import os
from dotenv import load_dotenv

from flask import Flask

from web_app.models import db, migrate
from web_app.routes.admin_routes import admin_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.iris_routes import iris_routes
from web_app.routes.stats_routes import stats_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="sqlite:///web_app_12.db")
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(admin_routes)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(iris_routes)
    app.register_blueprint(stats_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
