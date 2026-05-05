from datetime import timedelta
import os

from dotenv import load_dotenv
from flask import Flask, jsonify

from routes import register_routes


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")

    is_prod = os.getenv("FLASK_ENV") == "production"
    app.config["SESSION_PERMANENT"] = True
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)
    app.config.update(
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=is_prod,
    )

    @app.errorhandler(404)
    def not_found(_e):
        return jsonify({"error": "This route does not exist"}), 404

    @app.errorhandler(500)
    def server_error(_e):
        return jsonify({"error": "Internal server error. Our bad!"}), 500

    register_routes(app)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

