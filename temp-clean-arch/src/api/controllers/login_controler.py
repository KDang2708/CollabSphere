#Logincontroller for login.html
from flask import Blueprint, request, jsonify
from services.auth_service import AuthService       
from infrastructure.repositories.auth_repository import AuthRepository
from api.schemas.auth import LoginUserRequestSchema, LoginUserResponseSchema

from infrastructure.databases.mssql import session
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
auth_service = AuthService(AuthRepository(session))
login_request_schema = LoginUserRequestSchema()
login_response_schema = LoginUserResponseSchema()
