# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


from flask import request, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_raw_jwt
)
from flask_restplus import Resource

from ..blk import blk_user
from ..ext import crypt
from ..models.user import UserModel


class Register(Resource):
    """
    Register.
    """

    def post(self):
        """
        Endpoint to Register a new user.

        :return:
        """

        current_app.logger.info("GET Call from IMDB-Project - USER")

        user_info = request.get_json()
        print(user_info, 'user_info')

        if UserModel.find_by_username(user_info['username']):
            return {"message": "Username already exists"}, 400

        user = UserModel(**user_info)
        user.save_to_db()

        return {"message": "User created successfully"}, 201


class Manage(Resource):
    """
    User.
    """

    @classmethod
    def get(cls, user_id: int):
        """
        Endpoint to get the user details.

        :param user_id:
        :return:
        """

        current_app.logger.info("GET Call from IMDB-Project - USER")

        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404

        return user.json(), 200

    @classmethod
    def delete(cls, user_id: int):
        """
        Endpoint to delete the given user details.

        :param user_id:
        :return:
        """

        current_app.logger.info("DEL Call from IMDB-Project - USER")

        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404

        user.delete_from_db()
        return {"message": "User deleted successfully"}, 200


class Login(Resource):
    """
    Login.
    """

    def post(self):
        """
        Endpoint to login.

        :return:
        """

        current_app.logger.info("GET Call from IMDB-Project - LOGIN")

        user_info = request.get_json()
        user = UserModel.find_by_username(user_info['username'])
        if not user:
            return {'message': 'User Not Found'}, 404

        print('access_token', user.password_hash, 'refresh_token', user_info['password'])

        if crypt.check_password_hash(user.password_hash, user_info['password'].encode('utf-8')):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {'access_token': access_token, 'refresh_token': refresh_token}, 200

        return {"message": "Invalid Credentials!"}, 401


class Logout(Resource):
    """
    Logout.
    """

    @jwt_required
    def post(self):
        """
        Endpoint to logout

        :return:
        """

        jti = get_raw_jwt()['jti']
        blk_user.add(jti)

        return {"message": "Successfully logged out", 'jti': jti}, 200
