# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


import glob
import pickle
import time
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# save all tables ///--- one by one ---/// into separate sav files
tsv_files = glob.glob("../../data/*.tsv")
for file in tsv_files:
    print(file)
    pickle.dump(pd.read_table(file, sep="\t", low_memory=False, na_values=["\\N", "nan"]),
                open(file[:-4] + ".sav", "wb"))

print(time.ctime())

# df_ratings = pickle.load(open("../../data/title.ratings.sav","rb"))
# print(type(df_ratings.head()))

def find_value_in_other_columns(row_obj):
    if row_obj.nconst in row_obj.directors:
        if row_obj.nconst in row_obj.writers:
            return True
    return False

#
# -------------- ist----------------
# # name_basics = pd.read_csv('../../data/name.basics.tsv.gz', sep='\t', header=0)
# name_basics = pickle.load(open("../../data/name.basics.sav","rb"))
# movies_acted_by = name_basics[(name_basics.primaryName == 'Leonardo DiCaprio')].copy()
# movies_acted_by.set_index('nconst', inplace=True)
#
# print(movies_acted_by.columns)
# print(movies_acted_by[['primaryName', 'knownForTitles']])
# print(movies_acted_by.index)
# print(len(movies_acted_by.index))
#
#
# print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -11111----')
# # chunk = pd.read_csv('../../data/title.principals.tsv.gz', sep='\t', header=0)
# # chunk = pd.read_csv('../../data/title.principals.tsv.gz', sep='\t', header=0, chunksize=1000000)
# # title_principal = pd.concat(chunk)
# title_principal = pickle.load(open("../../data/title.principals.sav","rb"))
# title_info = title_principal[title_principal['category'] == 'actor'].copy()
# title_info.set_index('nconst', inplace=True)
#
# movies_with_person = movies_acted_by.join(title_info, how='inner')
# movies_with_person.set_index('tconst', inplace=True)
#
# print(movies_with_person.columns)
# print(movies_with_person.head())
#
# print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -11111----')
#
# print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -22222----')
# #
# # Title Basics w.r.t movies
# # title_basics = pd.read_csv('../../data/title.basics.tsv.gz', sep='\t', header=0)
# # chunk = pd.read_csv('../../data/title.basics.tsv.gz', sep='\t', header=0, chunksize=1000000)
# # title_basics = pd.concat(chunk)
# title_basics = pickle.load(open("../../data/title.basics.sav","rb"))
# movies_info = title_basics[(title_basics.titleType == 'movie')].copy()
# movies_info.set_index('tconst', inplace=True)
#
# # Ratings Basics
# # title_ratings = pd.read_csv('../../data/title.ratings.tsv.gz', sep='\t', header=0)
# # chunk = pd.read_csv('../../data/title.ratings.tsv.gz', sep='\t', header=0, chunksize=1000000)
# # title_ratings = pd.concat(chunk)
# title_ratings = pickle.load(open("../../data/title.ratings.sav","rb"))
# title_ratings.set_index('tconst', inplace=True)
#
# movies_with_rating = movies_info.join(title_ratings, how='inner')
# print(movies_with_rating.columns)
# print(movies_with_rating.head())
#
# print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -33333----')
# movies_with_person_title_rating = movies_with_rating.join(movies_with_person, how='inner')
# print(movies_with_person_title_rating.columns)
# # print(movies_with_person_title_rating)
#
# print(movies_with_person_title_rating[['primaryTitle', 'averageRating']])
# print(movies_with_person_title_rating.index)
# print(len(movies_with_person_title_rating.index))
# print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -44444----')
# print(time.ctime())
# -------------- 1st----------------


# # -------------- 2st----------------
# title_basics = pickle.load(open("../../data/title.basics.sav", "rb"))
# movies_info = title_basics[(title_basics.titleType == 'movie')].copy()
# movies_info.set_index('tconst', inplace=True)
#
# import warnings
#
# warnings.filterwarnings("ignore")
# movies_with_runtime = movies_info[movies_info.runtimeMinutes.notnull()]
# # movies_with_runtime["runtimeMinutes"] = movies_with_runtime.runtimeMinutes.astype(int)
# movies_with_runtime = movies_with_runtime[movies_with_runtime.runtimeMinutes.astype(int) > 300]
# print(movies_with_runtime.columns)
# print(movies_with_runtime[['primaryTitle', 'runtimeMinutes']])
# # -------------- 2st----------------


# # -------------- 2st----------------
# name_basics = pickle.load(open("../../data/name.basics.sav", "rb"))
# name_basics.set_index('nconst', inplace=True)
# # [10517589 rows x 2 columns]
# name_basics = name_basics[name_basics.primaryProfession.notnull()]
# # name_basics = pd.Series(name_basics)
#
# name_basics = name_basics[name_basics.primaryProfession.str.contains('writer') &
#                           name_basics.primaryProfession.str.contains('director') &
#                           name_basics.primaryProfession.str.contains('actor')
#                           ]
# print(name_basics.columns)
# print(name_basics[['primaryName', 'primaryProfession']])
#
#
# # -------------- 2st----------------
# name_basics = pickle.load(open("../../data/name.basics.sav", "rb"))
# # title_principal.set_index('nconst', inplace=True)

# print(time.ctime())
# # -------------- 3rd----------------
# title_basics = pickle.load(open("../../data/title.basics.sav", "rb"))
# movies_info = title_basics[(title_basics.titleType == 'movie')].copy()
# # movies_info.set_index('tconst', inplace=True)
#
# movie_ratings = pickle.load(open("../../data/title.ratings.sav", "rb"))
# # movie_ratings.set_index('tconst', inplace=True)
#
# movie_crew = pickle.load(open("../../data/title.crew.sav", "rb"))
# # movie_crew.set_index('tconst', inplace=True)
#
# title_principal = pickle.load(open("../../data/title.principals.sav", "rb"))
# # title_principal.set_index('tconst', inplace=True)
#
# name_basics = pickle.load(open("../../data/name.basics.sav", "rb"))
# # name_basics.set_index('nconst', inplace=True)
#
# movies_dataset = pd.merge(pd.merge(pd.merge(pd.merge(movies_info, movie_ratings, on="tconst"),
#                                        movie_crew, on="tconst"),
#                               title_principal, on="tconst"),
#                      name_basics, on="nconst")
#
# pickle.dump(movies_dataset, open('../../data/only_movie.sav', "wb"))
#
# print(movies_dataset.head())
# print(movies_dataset.columns)
# print(movies_dataset[['titleType', 'directors', 'primaryName']])

# -------------- 3rd----------------
print(time.ctime())
# # -------------- 3rd--------------

print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -44444----')
movies_dataset = pickle.load(open("../../data/name.basics.csv", "rb"))
movies_dataset = movies_dataset[movies_dataset.writers.notnull() & movies_dataset.directors.notnull()]
# movies_dataset = movies_dataset[(movies_dataset.writers.str.contains(movies_dataset.primaryName)) &
#                                 (movies_dataset.directors.str.contains(movies_dataset.primaryName))]

# name_basics.primaryProfession.str.contains('writer')
# [2066426 rows x 4 columns]

# print(movies_dataset.head())
# print(movies_dataset.columns)
# print(movies_dataset[['primaryTitle', 'primaryName', 'directors', 'writers']])

df1 = movies_dataset[[ 'primaryTitle', 'primaryName', 'nconst', 'directors', 'writers']]
print(df1.head())

print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -44444----')

print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -11111----')


df2 = df1[[x[0] in x[1] for x in zip(df1['nconst'], df1['writers'])]][['primaryTitle', 'primaryName', 'nconst', 'directors', 'writers']]
df2 = df2[[x[0] in x[1] for x in zip(df2['nconst'], df2['directors'])]][['primaryTitle', 'primaryName', 'nconst', 'directors', 'writers']]


# df2 = df1[df1.apply(find_value_in_other_columns, axis=1)][['primaryTitle', 'primaryName', 'nconst', 'directors', 'writers']]


# mask = df1.eq(df1.pop('nconst'), axis=0)

# df2["inall"] = df2.drop("nconst", 1).isin(df2["nconst"].to_list()).any(1)
# [149670 rows x 5 columns]

# Sun Nov 22 16:51:30 2020
#
# [149670 rows x 5 columns]
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -44444----
# Sun Nov 22 16:52:41 2020


# print(df2)

print(df2.head(10))
# print(movies_dataset[['primaryTitle', 'primaryName', 'directors', 'writers', "inall"]])
print('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -44444----')
# # -------------- 3rd----------------
print(time.ctime())
