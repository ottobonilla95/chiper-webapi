import datetime
from flask_restful import Resource
from flask import request
from models.user import UserModel
from schemas.user import UserSchema
from passlib.hash import pbkdf2_sha256

from flask_jwt_extended import (create_access_token,
                                get_jwt_identity,
                                create_refresh_token,
                                jwt_required,
                                jwt_refresh_token_required,
                                get_raw_jwt,
                                fresh_jwt_required)

import os

from libs.auditory import Auditory


user_schema = UserSchema()

timedelta = datetime.timedelta(minutes=5)
custom_pbkdf2 = pbkdf2_sha256.using(rounds=296411)


class UserRegister(Resource):
    def post(self):

        try:
            user_json = request.get_json()["userData"]
            user_json = request.get_json()["userData2"]

            user = user_schema.load(user_json)

            if UserModel.find_by_username(user.username):
                return {"message": "A user with that username already exists"}, 400

            if UserModel.find_by_email(user.email):
                return {"message": "A user with that email already exists"}, 400
         
            # Hash the password
            hashed_pass = custom_pbkdf2.hash(user.password)
            user.password = hashed_pass

            user.save_to_db()

            access_token = create_access_token(identity=user.id, fresh=True, expires_delta=timedelta)

            return {
                "message":"User created successfully!",
                "user":{ 
                    "user": user_schema.dump(user),
                    "userToken":{
                        "access_token":access_token
                    }
                },
            }
            
        except Exception as e:
            Auditory.log_error("WebApi", "Auth", "UserRegister", str(e))
            return {"message": "Error when creating the user"}, 500

class UserLogin(Resource):
    def post(self):

        try:
            user_recived = request.get_json()         
            userFound = UserModel.find_by_username_or_email(user_recived.get("username_email"))

            if userFound and custom_pbkdf2.verify(user_recived.get("password"), userFound.password):

                access_token = create_access_token(
                    identity=userFound.id, fresh=True, expires_delta=timedelta)


                return {
                    "message":"User Logged In",
                    "user":{ 
                        "user": user_schema.dump(userFound),
                        "userToken":{
                            "access_token":access_token
                        }
                    },
                }

            return {"message": "Invalid Credentials"}, 401

        except Exception as e:
            Auditory.log_error("WebApi", "Auth", "UserLogin", str(e))
            return {"message": "An error has occured"}, 500

