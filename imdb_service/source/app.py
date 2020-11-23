# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = "Sri Pandi, Satheesh Rathinakumar, Caleb Beard"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


import logging
from logging.handlers import TimedRotatingFileHandler

from flask_restful import Api

from .resources.movies import MoviesByActor, MoviesByPersonInAllThree
from .resources.movies import MoviesByActorWithRating, MoviesByRunningTime
from .resources.ping import Ping, Imdb
from .resources.user import Login, Logout
from .resources.user import Register, Manage


def start_service(app_object):
    """
    Start the service.

    :param app_object:
    :return:
    """

    # Get Log handler for App
    log_file = app_object.config["LOG_FILE"]
    initialize_logger(app_object, log_file)

    # Start the App
    app_object.logger.info("IMDB source is up and running")
    initialize_resources(app_object)


def initialize_logger(app_object, log_file=""):
    """
    Initialize logger.

    :param app_object:
    :param log_file:
    :return:
    """

    # Create Logger for App
    formatter = logging.Formatter("[%(asctime)s] : %(levelname)s - %(message)s")
    log_handler = TimedRotatingFileHandler(log_file, when="midnight")
    log_handler.setFormatter(formatter)

    # Set log level in handler
    log_handler.setLevel(logging.INFO)
    logging.getLogger("werkzeug").setLevel(logging.DEBUG)
    logging.getLogger("werkzeug").addHandler(log_handler)

    # Set log handler to source
    app_object.logger.addHandler(log_handler)
    app_object.logger.setLevel(logging.INFO)


def initialize_resources(app_object):
    """
    Initialize resource.

    :param app_object:
    :return:
    """

    # Initialize FLASK API object to add resources
    imdb_api = Api(app=app_object)
    imdb_api.init_app(app_object)

    # Add resources here
    imdb_api.add_resource(Imdb, "/")
    imdb_api.add_resource(Ping, "/ping")
    imdb_api.add_resource(Register, '/user/register')
    imdb_api.add_resource(Manage, '/user/<int:user_id>')
    imdb_api.add_resource(Login, '/user/login')
    imdb_api.add_resource(Logout, '/user/logout')

    imdb_api.add_resource(MoviesByActor, '/movies/actor/<actor_name>')
    imdb_api.add_resource(MoviesByPersonInAllThree, '/movies/allthree')
    imdb_api.add_resource(MoviesByRunningTime, '/movies/runtime/<time_in_hours>')
    imdb_api.add_resource(MoviesByActorWithRating, '/movies/actor/<actor_name>/<best_or_worst>')
