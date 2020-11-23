# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_jwt_extended import JWTManager
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()
# login_manager = LoginManager()
jwt = JWTManager()
crypt = Bcrypt()
