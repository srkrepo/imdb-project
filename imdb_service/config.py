# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import os
from datetime import timedelta

from dotenv import load_dotenv


class BaseConfig(object):
    """
    Common configurations
    """

    # ---------------------------------- App Config --------------------------------
    load_dotenv()
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    APPS_DIR = os.path.dirname(BASE_DIR)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = "RmHGYVmlRnCMkIa5A003a0CR5mm"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    TIME_DELAY = 1  # In minutes
    SQLALCHEMY_ECHO = True
    # ---------------------------------- App Config --------------------------------

    # ---------------------------------- Log Config --------------------------------
    ARCHIVE_FOLDER = os.path.join(BASE_DIR, "data")
    LOG_FOLDER = os.path.join(ARCHIVE_FOLDER, "logs")
    LOG_FILE = os.path.join(LOG_FOLDER, "imdb.log")
    # ---------------------------------- Log Config --------------------------------


class ProductionConfig(BaseConfig):
    """
    Production configurations
    """

    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """

    # ---------------------------------- App Config --------------------------------
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 15
    # ---------------------------------- App Config --------------------------------

    # ---------------------------------- Database Config ---------------------------
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}/data/imdb.db".format(BASE_DIR)
    # ---------------------------------- Database Config ---------------------------

    # ---------------------------------- Database Config ---------------------------
    JWT_SECRET_KEY='RnCMkIa5YVmlRnCMkIa5A003a0Ia5YVm'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS  = ['access', 'refresh']
    # ---------------------------------- Database Config ---------------------------


APP_CONFIG = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
