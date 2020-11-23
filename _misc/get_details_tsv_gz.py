# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import pandas as pd

# import pickle

# imdb_basic_dataset = pd.read_csv('../../data/name.basics.tsv', delimiter = '\t', engine='python', quoting = 3)
# #
# # df_ratings = pickle.load(open("../../data/name.basics.tsv","rb"))
# # print(df_ratings.head(), '**************')
#
# print(imdb_basic_dataset.head())

import time
print(time.ctime())
# Name Basics
pd.set_option('max_columns', 7)

name_basics = pd.read_csv('../../data/name.basics.tsv.gz', sep='\t', header=0)
movies_acted_by = name_basics[(name_basics.primaryName == 'Leonardo DiCaprio')].copy()
movies_acted_by.set_index('nconst', inplace=True)

print(movies_acted_by.columns)
print(movies_acted_by[['primaryName', 'knownForTitles']])
print(movies_acted_by.index)
print(len(movies_acted_by.index))

#
print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -11111----')
chunk = pd.read_csv('../../data/title.principals.tsv.gz', sep='\t', header=0, chunksize=1000000)
title_principal = pd.concat(chunk)
title_info = title_principal[title_principal['category'] == 'actor'].copy()
title_info.set_index('nconst', inplace=True)

movies_with_person = movies_acted_by.join(title_info, how='inner')
movies_with_person.set_index('tconst', inplace=True)

print(movies_with_person.columns)
print(movies_with_person.head())

print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -11111----')

print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -22222----')
#
# Title Basics w.r.t movies
# title_basics = pd.read_csv('../../data/title.basics.tsv.gz', sep='\t', header=0)
chunk = pd.read_csv('../../data/title.basics.tsv.gz', sep='\t', header=0, chunksize=1000000)
title_basics = pd.concat(chunk)
movies_info = title_basics[(title_basics.titleType == 'movie')].copy()
movies_info.set_index('tconst', inplace=True)

# Ratings Basics
# title_ratings = pd.read_csv('../../data/title.ratings.tsv.gz', sep='\t', header=0)
chunk = pd.read_csv('../../data/title.ratings.tsv.gz', sep='\t', header=0, chunksize=1000000)
title_ratings = pd.concat(chunk)
title_ratings.set_index('tconst', inplace=True)

movies_with_rating = movies_info.join(title_ratings, how='inner')
print(movies_with_rating.columns)
print(movies_with_rating.head())

print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -33333----')
movies_with_person_title_rating = movies_with_rating.join(movies_with_person, how='inner')
print(movies_with_person_title_rating.columns)
# print(movies_with_person_title_rating)

print(movies_with_person_title_rating[['primaryTitle', 'averageRating']])
print(movies_with_person_title_rating.index)
print(len(movies_with_person_title_rating.index))
print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -44444----')
print(time.ctime())
