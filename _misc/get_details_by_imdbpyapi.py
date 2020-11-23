# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie
movie = ia.get_movie('0133093')
# people = ia.search_person('angelina')
#
#
# print(people)
#
# # print the names of the directors of the movie
# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])
#
# # print the genres of the movie
# print('Genres:')
# for genre in movie['genres']:
#     print(genre)

# search for a person name
actor_code = None
people = ia.search_person('Leonardo DiCaprio')
for person in people:
    actor_code = person.personID
    print(person.personID, person['name'])

# getting information
actor_results = ia.get_person_filmography(actor_code)

print('actor_results', actor_results)
# printing movie name
# tt0993846,tt1375666,tt0407887,tt0120338

movie_name = actor_results['data']['filmography']['actor']
print(len(movie_name))
