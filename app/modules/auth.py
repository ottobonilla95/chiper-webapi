from flask import Blueprint
from flask_restful import Api
from resources.auth.user import (
    UserRegister,
    UserLogin,
    # TokenRefresh,
    )

# Create bluepirnt
auth_module = Blueprint('auth', __name__)
api = Api(auth_module)

# Add resources
# signup
api.add_resource(UserRegister, '/signup')

# login
api.add_resource(UserLogin, '/login')


# # UserTokenRefresh
# api.add_resource(TokenRefresh, '/tokenrefresh')





