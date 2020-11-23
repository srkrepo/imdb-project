# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from imdb_service.source import initialize_and_start_app
from imdb_service.source.ext import db as imdb_db

imdb_app = initialize_and_start_app()

if __name__ == '__main__':
    print('Call from RUN, the main File')

    migrate = Migrate(imdb_app, imdb_db)
    manager = Manager(imdb_app)

    manager.add_command('db', MigrateCommand)
    manager.run()

    imdb_app.run(host='0.0.0.0')
