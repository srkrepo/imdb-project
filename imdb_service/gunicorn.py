# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


ssl_context = 'adhoc'
bind = '0.0.0.0:9090'
accesslog = './data/logs/gunicorn-access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" in %(D)sµs'
worker = 5
timeout = 30000
pidfile = 'imdb.pid'
worker_class = 'gthread'
workers = 2
worker_connections = 1000
keepalive = 2
threads = 4
proc_name = 'imdb'
backlog = 2048
errorlog = '-'
