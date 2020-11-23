# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import gc
import os
import pickle
import time
import warnings

import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
APPS_DIR = os.path.dirname(BASE_DIR)

DATA_FILE_PATH = os.path.join(APPS_DIR, 'data')

gc.collect()
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)


def get_movies_by_actor(actor_name=None):
    """
    Module used to get Movies by an actor.
    This  wll return movie with rating "MOVIE  ## RATING"

    :param actor_name:
    :return:
    """

    status, message, lst_movies, num_movies = False, '', {"HEADING": "MOVIE  ## RATING"}, 0

    if 1:
        if not actor_name:
            raise Exception("Invalid input(Actor Name)")

        name_basics = pickle.load(open(os.path.join(DATA_FILE_PATH, "name.basics.sav"), "rb"))
        movies_acted_by = name_basics[(name_basics.primaryName.str.lower() == actor_name)].copy()
        movies_acted_by.set_index('nconst', inplace=True)

        title_principal = pickle.load(open(os.path.join(DATA_FILE_PATH, "title.principals.sav"), "rb"))
        title_info = title_principal[title_principal['category'] == 'actor'].copy()
        title_info.set_index('nconst', inplace=True)

        movies_with_person = movies_acted_by.join(title_info, how='inner')
        movies_with_person.set_index('tconst', inplace=True)

        title_basics = pickle.load(open(os.path.join(DATA_FILE_PATH, "title.basics.sav"), "rb"))
        movies_info = title_basics[(title_basics.titleType == 'movie')].copy()
        movies_info.set_index('tconst', inplace=True)

        title_ratings = pickle.load(open(os.path.join(DATA_FILE_PATH, "title.ratings.sav"), "rb"))
        title_ratings.set_index('tconst', inplace=True)

        movies_with_rating = movies_info.join(title_ratings, how='inner')
        movies_with_person_title_rating = movies_with_rating.join(movies_with_person, how='inner')

        df1 = movies_with_person_title_rating[['primaryTitle', 'averageRating']]
        df2 = df1['primaryTitle'].astype(str) + " ## " + df1["averageRating"].astype(str)

        num_movies = len(df2.index)

        _movies = df2.to_dict()
        lst_movies = {**lst_movies, **_movies}

        status, message = True, 'Data analysed successfully'

    # except Exception as err_msg:
    #     message = str(err_msg)

    return status, message, lst_movies, num_movies


def get_five_rated_movies_by_actor(actor_name=None, best_or_worst=None):
    """
    Module used to get Top 5 BEST/WORST rated Movies by an actor.
    This wll return movie with rating "MOVIE  ## RATING"

    :param actor_name:
    :param best_or_worst:
    :return:
    """

    status, message, lst_movies = False, '', {"HEADING": "MOVIE  ## RATING"}

    try:
        if not actor_name:
            raise Exception("Invalid input(Actor Name)")

        if best_or_worst.lower() not in ['best', 'worst']:
            raise Exception("In valid option, It should be 'best/worst'")

        name_basics = pickle.load(open(os.path.join(DATA_FILE_PATH, "name.basics.sav"), "rb"))
        movies_acted_by = name_basics[(name_basics.primaryName.str.lower() == actor_name)].copy()
        movies_acted_by.set_index('nconst', inplace=True)

        title_principal = pickle.load(open(os.path.join(DATA_FILE_PATH, "title.principals.sav"), "rb"))
        title_info = title_principal[title_principal['category'] == 'actor'].copy()
        title_info.set_index('nconst', inplace=True)

        movies_with_person = movies_acted_by.join(title_info, how='inner')
        movies_with_person.set_index('tconst', inplace=True)

        title_basics = pickle.load(open(os.path.join(DATA_FILE_PATH, "title.basics.sav"), "rb"))
        movies_info = title_basics[(title_basics.titleType == 'movie')].copy()
        movies_info.set_index('tconst', inplace=True)

        title_ratings = pickle.load(open(os.path.join(DATA_FILE_PATH, "title.ratings.sav"), "rb"))
        title_ratings.set_index('tconst', inplace=True)

        movies_with_rating = movies_info.join(title_ratings, how='inner')
        movies_with_person_title_rating = movies_with_rating.join(movies_with_person, how='inner')

        df1 = movies_with_person_title_rating[['primaryTitle', 'averageRating']]

        if best_or_worst.lower() == 'worst':
            df1 = df1.sort_values("averageRating", ascending=True).head(5)
        else:
            df1 = df1.sort_values("averageRating", ascending=False).head(5)

        df2 = df1['primaryTitle'].astype(str) + " ## " + df1["averageRating"].astype(str)

        _movies = df2.to_dict()
        lst_movies = {**lst_movies, **_movies}

        status, message = True, 'Data analysed successfully'

    except Exception as err_msg:
        message = str(err_msg)

    return status, message, lst_movies


def get_top_rated_movies_person_in_all_three():
    """
    Module used to get Top 25 BEST rated Movies by a single person was a writer, director, and also
    one of the actors.
    This wll return movie with rating "MOVIE ## PERSON ## RATING"

    :return:
    """

    status, message, lst_movies = False, '', {"HEADING": "MOVIE ## PERSON ## RATING"}

    try:
        movies_dataset = pickle.load(open(os.path.join(DATA_FILE_PATH, "name.basics.csv"), "rb"))
        movies_dataset = movies_dataset[movies_dataset.writers.notnull() & movies_dataset.directors.notnull()]

        df1 = movies_dataset[['primaryTitle', 'primaryName', 'nconst', 'directors', 'writers', 'averageRating']]

        df2 = df1[[x[0] in x[1] for x in zip(df1['nconst'], df1['writers'])]][
            ['primaryTitle', 'primaryName', 'averageRating', 'nconst', 'directors', 'writers']]
        df2 = df2[[x[0] in x[1] for x in zip(df2['nconst'], df2['directors'])]][
            ['primaryTitle', 'primaryName', 'averageRating', 'nconst', 'directors', 'writers']]

        df2 = df2.sort_values("averageRating", ascending=False)

        df3 = df2['primaryTitle'].astype(str) + " ## " + df2["primaryName"].astype(str) \
              + " ## " + df2["averageRating"].astype(str)

        _movies = df3.iloc[:25].to_dict()
        lst_movies = {**lst_movies, **_movies}

        status, message = True, 'Data analysed successfully'

    except Exception as err_msg:
        message = str(err_msg)

    return status, message, lst_movies


def get_movies_by_running_time(time_in_hours):
    """
    Module used to get the movies which are longer than given hours.
    This wll return movie with rating "MOVIE  ## TIME(HH:MM)"

    :param time_in_hours:
    :return:
    """

    status, message, lst_movies = False, '', {"HEADING": "MOVIE  ## TIME(HH:MM)"}

    try:
        time_in_minutes = int(time_in_hours) * 60
        if not time_in_minutes:
            raise Exception("Invalid input(time)")

        title_basics = pickle.load(open(os.path.join(DATA_FILE_PATH, "title.basics.sav"), "rb"))
        movies_info = title_basics[(title_basics.titleType == 'movie')].copy()
        movies_info.set_index('tconst', inplace=True)

        movies_with_runtime = movies_info[movies_info.runtimeMinutes.notnull()]
        movies_with_runtime = movies_with_runtime[movies_with_runtime.runtimeMinutes.astype(int) >= time_in_minutes]
        movies_with_runtime['runningTime'] = pd.to_datetime(movies_with_runtime.runtimeMinutes, unit='m').dt.strftime(
            '%H:%M')

        df1 = movies_with_runtime[['primaryTitle', 'runningTime']]
        df2 = df1['primaryTitle'].astype(str) + " ## " + df1["runningTime"].astype(str)

        _movies = df2.to_dict()
        lst_movies = {**lst_movies, **_movies}

        status, message = True, 'Data analysed successfully'

    except Exception as err_msg:
        message = str(err_msg)

    return status, message, lst_movies


# print(time.ctime())
# print(get_top_rated_movies_person_in_all_three())
# print(time.ctime())
#
# print(get_movies_by_running_time('7'))

# print(time.ctime())
# print(get_movies_by_actor('leonardo dicaprio'))
# print(time.ctime())

# print(get_five_rated_movies_by('leonardo dicaprio', 'worst'))
# print(time.ctime())
#
# x = {'tt1375666': 'Inception ## 8.8', 'tt0407887': 'The Departed ## 8.5', 'tt1853728': 'Django Unchained ## 8.4',
#      'tt1130884': 'Shutter Island ## 8.2', 'tt0993846': 'The Wolf of Wall Street ## 8.2'}
# {'tt0119004': "Don's Plum ## 5.8", 'tt0120533': 'Celebrity ## 6.3', 'tt0114214': 'The Quick and the Dead ## 6.4',
#  'tt1616195': 'J. Edgar ## 6.5', 'tt0120744': 'The Man in the Iron Mask ## 6.5'}
