# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from source import initialize_and_start_app

imdb_app = initialize_and_start_app()

if __name__ == "__main__":
    imdb_app.run()
