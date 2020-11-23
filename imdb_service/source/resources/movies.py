# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


from flask import current_app
from flask_restplus import Resource

from ..core.movies_info import get_five_rated_movies_by_actor, get_movies_by_running_time
from ..core.movies_info import get_movies_by_actor, get_top_rated_movies_person_in_all_three


class MoviesByActor(Resource):
    """
    MoviesByActor.
    """

    def get(self, actor_name):
        """
        Endpoint used to get Movies by an actor.

        :param actor_name:
        :return:
        """

        current_app.logger.info("GET Call from IMDB-Project - By an ACTOR")
        print("GET Call from IMDB-Project - By an ACTOR")
        response_object, response_status = {"message": "GET Call from IMDB-Project - "
                                                       "By an ACTOR"}, 500

        try:
            status, message, lst_movies, num_movies = get_movies_by_actor(actor_name)
            if not status:
                current_app.logger.error("Message: {}".format(message))
                raise Exception(message)

            current_app.logger.info("Message: {}".format(message))
            response_object, response_status = {'Movies_with_rating': lst_movies, 'Number_of_Movies': num_movies}, 200
        except Exception as err_msg:
            response_object, response_status = {"message": str(err_msg)}, 500

        return response_object, response_status


class MoviesByActorWithRating(Resource):
    """
    MoviesByActorWithRating.
    """

    def get(self, actor_name, best_or_worst):
        """
        Endpoint used to get Top 5 BEST/WORST rated Movies by an actor.

        :param actor_name:
        :param best_or_worst:
        :return:
        """

        current_app.logger.info("GET Call from IMDB-Project - By an ACTOR woth Rating worst/best")
        print("GET Call from IMDB-Project - By an ACTOR woth Rating worst/best")
        response_object, response_status = {"message": "GET Call from IMDB-Project - "
                                                       "By an ACTOR woth Rating worst/best"}, 500

        try:
            status, message, lst_movies = get_five_rated_movies_by_actor(actor_name, best_or_worst)
            if not status:
                current_app.logger.error("Message: {}".format(message))
                raise Exception(message)

            current_app.logger.info("Message: {}".format(message))
            response_object, response_status = {'Five_{}_Rated_Movies'.format(best_or_worst.title()): lst_movies}, 200
        except Exception as err_msg:
            response_object, response_status = {"message": str(err_msg)}, 500

        return response_object, response_status


class MoviesByRunningTime(Resource):
    """
    MoviesByRunningTime.
    """

    # @jwt_required
    def get(self, time_in_hours):
        """
        Endpoint used to get the movies which are longer than given hours.

        :param time_in_hours:
        :return:
        """

        current_app.logger.info("GET Call from IMDB-Project - By running time")
        print("GET Call from IMDB-Project - By running time")
        response_object, response_status = {"message": "GET Call from IMDB-Project - "
                                                       "By running time"}, 500

        try:
            status, message, lst_movies = get_movies_by_running_time(time_in_hours)
            if not status:
                current_app.logger.error("Message: {}".format(message))
                raise Exception(message)

            current_app.logger.info("Message: {}".format(message))
            response_object, response_status = {'Movies_with_running_time': lst_movies}, 200
        except Exception as err_msg:
            response_object, response_status = {"message": str(err_msg)}, 500

        return response_object, response_status


class MoviesByPersonInAllThree(Resource):
    """
    MoviesByPersonInAllThree.
    """

    def get(self):
        """
        Endpoint used to get Top 25 BEST rated Movies by a single person was a writer, director, and also
        one of the actors

        :return:
        """

        current_app.logger.info(
            "GET Call from IMDB-Project - By a single person was a writer, director, and also one of the actors")
        print("GET Call from IMDB-Project - By a single person was a writer, director, and also one of the actors")

        response_object, response_status = {"message": "GET Call from IMDB-Project - By a single person was a writer, "
                                                       "director, and also one of the actors"}, 500

        try:
            status, message, lst_movies = get_top_rated_movies_person_in_all_three()
            if not status:
                current_app.logger.error("Message: {}".format(message))
                raise Exception(message)

            current_app.logger.info("Message: {}".format(message))
            response_object, response_status = {'Top_Rated_Movies': lst_movies}, 200
        except Exception as err_msg:
            response_object, response_status = {"message": str(err_msg)}, 500

        return response_object, response_status
