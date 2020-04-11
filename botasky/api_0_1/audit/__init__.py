#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Created on 2019-7-22


@module: api_0_1/audit
@used: modify audit
"""

from flask import Blueprint
api = Blueprint('api_audit', __name__)

from . import alter

__all__ = ['']
__author__ = 'zhihao'