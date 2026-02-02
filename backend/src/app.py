from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

from flask import Flask, jsonify
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint

from infrastructure.databases.factory_database import FactoryDatabase
from infrastructure.repositories.todo_repository import TodoRepository
from services.todo_service import TodoService
from api.controllers.todo_controller import create_todo_blueprint
from api.controllers.auth_controller import auth_bp
from api.swagger import spec
from api.middleware import middleware


def create_app():
    app = Flask(__name__)
    Swagger(app)

    # ===== DATABASE =====
    db = FactoryDatabase.get_database("POSTGRES")

    # ===== DEPENDENCIES =====
    todo_repo = TodoRepository(db.session)
    todo_service = TodoService(todo_repo)

    # ===== BLUEPRINTS =====
    app.register_blueprint(create_todo_blueprint(todo_service))
    app.register_blueprint(auth_bp)

    middleware(app)

    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=9999, debug=True)
