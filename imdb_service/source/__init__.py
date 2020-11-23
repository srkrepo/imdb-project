# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


import os

from flask import Flask, jsonify
from flask_cors import CORS

from .app import start_service
from .blk import blk_user
from .ext import jwt, db, crypt
from ..config import APP_CONFIG


def initialize_and_start_app():
    """

    :return:
    """

    # Set base source
    imdb_app = Flask(__name__, instance_relative_config=True)
    # env = Environment(imdb_app)

    # Get and set Configuration
    config_mode = os.getenv('FLASK_ENV')
    imdb_app.config.from_object(APP_CONFIG[config_mode])

    # CORS
    CORS(imdb_app)

    # Extensions
    db.init_app(imdb_app)
    jwt.init_app(imdb_app)
    crypt.init_app(imdb_app)

    # Validate App Configuration
    print('config_mode', config_mode)
    start_service(imdb_app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return decrypted_token['identity'] in blk_user

    @jwt.expired_token_loader
    def expired_token_callback():
        return jsonify({
            'message': 'The token has expired.',
            'error': 'token_expired'
        }), 401

    return imdb_app
