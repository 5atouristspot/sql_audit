#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Created on 2017-12-01


@module: gun
@used: gunicorn config
"""

import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

debug = False
loglevel = 'debug'
bind = '10.20.4.110:3621'
pidfile = 'botasky.pid'
logfile = 'log/gunicorn_debug.log'

#number of run processes
workers = int(multiprocessing.cpu_count())
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

#curl interface timeout
timeout = 30000

x_forwarded_for_header = 'X-FORWARDED-FOR'
