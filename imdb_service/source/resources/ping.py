# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


from flask import current_app
from flask_restplus import Resource


class Ping(Resource):
    """
    Ping.
    """

    def get(self):
        """
        End point for health check.

        :return:
        """

        current_app.logger.info("GET Call from IMDB-Project - PING")
        return {'message': 'Pong..!'}, 200


class Imdb(Resource):
    """
    Ping.
    """

    def get(self):
        """
        Dummy Endpoint.

        :return:
        """

        current_app.logger.info("GET Call from IMDB-Project - PING")
        return {'message': 'Welcome..!'}, 200