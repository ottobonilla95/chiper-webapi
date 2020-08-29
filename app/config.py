import os
# sql alchemy
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI")

# JWT
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')


