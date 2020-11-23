# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

import glob
import gzip
import os
import pickle
import shutil
from urllib.request import urlopen

import pandas as pd

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FILES_TO_BE_DOWNLOADED = ['title.akas.tsv.gz', 'title.basics.tsv.gz', 'title.crew.tsv.gz', 'title.principals.tsv.gz',
                          'title.ratings.tsv.gz', 'name.basics.tsv.gz']

# FILES_TO_BE_DOWNLOADED = ['title.episode.tsv.gz']


def unzip_imdb_dataset():
    """
    This is used to download and unzip the imdb dataset
    :return:
    """

    message = ""

    # Download, UnZip the tsv.gz and move file as .sav
    try:
        for _file in FILES_TO_BE_DOWNLOADED:
            imdb_url = 'https://datasets.imdbws.com/{}'.format(_file)

            with urlopen(imdb_url) as response:
                print(response.status)
                if not response.status == 200:
                    raise Exception('Failed to download "{}". HTTP response code: {}'.format(imdb_url, response.status))

                with open(_file, 'wb') as f:
                    shutil.copyfileobj(response, f)

        gz_files = glob.glob("*.tsv.gz")
        for gz_file in gz_files:
            un_gz_file = '{}.tsv'.format(gz_file[:-7])
            print("Unzipping {} to {} ".format(gz_file, un_gz_file))
            with gzip.open(gz_file, 'rb') as fobj_in:
                with open(un_gz_file, 'wb') as fobj_out:
                    shutil.copyfileobj(fobj_in, fobj_out)

        # Convert the file .tsv to .sav file for better processing
        tsv_files = glob.glob("*.tsv")
        for in_file in tsv_files:
            out_file = os.path.join('dataset', "{}.sav".format(in_file[:-4]))
            pickle.dump(pd.read_table(in_file, sep="\t", low_memory=False, na_values=["\\N", "nan"]),
                        open(out_file, "wb"))

        # -------------------  MERGE All Dataset in to Single Dataset ------------
        title_basics = pickle.load(open("dataset/title.basics.sav", "rb"))
        movies_info = title_basics[(title_basics.titleType == 'movie')].copy()
        # movies_info.set_index('tconst', inplace=True)

        movie_ratings = pickle.load(open("dataset/title.ratings.sav", "rb"))
        # movie_ratings.set_index('tconst', inplace=True)

        movie_crew = pickle.load(open("dataset/title.crew.sav", "rb"))
        # movie_crew.set_index('tconst', inplace=True)

        title_principal = pickle.load(open("dataset/title.principals.sav", "rb"))
        # title_principal.set_index('tconst', inplace=True)

        name_basics = pickle.load(open("dataset/name.basics.sav", "rb"))
        # name_basics.set_index('nconst', inplace=True)

        movies_dataset = pd.merge(pd.merge(pd.merge(pd.merge(movies_info, movie_ratings, on="tconst"),
                                                    movie_crew, on="tconst"),
                                           title_principal, on="tconst"),
                                  name_basics, on="nconst")

        pickle.dump(movies_dataset, open('dataset/name.basics.sav'[:-4] + ".csv", "wb"))
        # -------------------  MERGE All Dataset in to Single Dataset ------------

        message = "Files unzipped/renamed successfully"

    except Exception as err_msg:
        message = str(err_msg)

    return message


if __name__ == "__main__":
    print(unzip_imdb_dataset())
