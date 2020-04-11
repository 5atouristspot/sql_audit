#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Created on 2019-7-22


@module: database
@used:  add database , user grants
"""
from . import api
from flask import request, jsonify, Response
import json
from botasky.utils.MyCONN import MySQL

from botasky.utils.MyFILE import project_abdir, recursiveSearchFile
from botasky.utils.MyLOG import MyLog
logConfig = recursiveSearchFile(project_abdir, '*logConfig.ini')[0]
mylog = MyLog(logConfig, 'database.py')
logger = mylog.outputLog()

import ConfigParser
config = ConfigParser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)

import random
import string

__all__ = ['database']
__author__ = 'zhihao'

@api.route('/database', methods=['GET', 'POST'])
def database():
    '''
    :put in: port
    :put in: database
    '''
    try:
        port = request.args.get('port', type=int, default=None)
        database = request.args.get('database', type=str, default='inception_test')
        #sql_statment = sql_statment.decode('ascii')
        #sql_statment = urllib.quote(sql_statment.encode('utf-8', 'replace'))
        #print port
        #print database
        #print sql_statment

        sql_use_port_get_ip = "select ip from port_ip_relation where port = {port} and deleteflag = 0;".format(port=port)
        dbconfig = {'host': config.get('META', 'host'),
                    'port': int(config.get('META', 'port')),
                    'user': config.get('META', 'user'),
                    'passwd': config.get('META', 'pwd'),
                    'db': config.get('META', 'db'),
                    'charset': 'utf8'}
        db = MySQL(dbconfig)
        db.query(sql_use_port_get_ip)
        db.commit()
        result_info = db.fetchOneRow()
        result_infos = db.fetchAllRows()
        db.close()

        #create database
        if result_info is not None:
            ip_info = result_info[0]
            #print ip_info
        else:
            ip_info = ''
            #print ip_info

        dbconfig_db = {'host': ip_info,
                    'port': port,
                    'user': 'djyv4_rw',
                    'passwd': 'tfkj_secret',
                    'db': 'mysql',
                    'charset': 'utf8'}

        sql_create_database = "create database {database};".format(database=database)
        db_create_database = MySQL(dbconfig_db)
        db_create_database.query(sql_create_database)
        db_create_database.commit()
        create_database_info = db_create_database.fetchOneRow()
        db_create_database.close()

        #create user and grants

        new_pwd = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        #print(new_pwd)

        for result_infos in result_info:
            if result_info is not None:
                ip_info = result_info[0]
                # print ip_info
            else:
                ip_info = ''
                # print ip_info

            dbconfig_db = {'host': ip_info,
                           'port': port,
                           'user': 'djyv4_rw',
                           'passwd': 'tfkj_secret',
                           'db': 'mysql',
                           'charset': 'utf8'}

            sql_create_user = "CREATE USER {database}_rw@'10.20.4.%' IDENTIFIED BY '{new_pwd}'; " \
                              "GRANT USAGE,SELECT,INSERT,UPDATE ON {database}.* TO {database}_rw@'10.20.4.%' WITH GRANT OPTION;" \
                              "CREATE USER {database}_rw@'192.168.%' IDENTIFIED BY '{new_pwd}';" \
                              "GRANT USAGE,SELECT,INSERT,UPDATE ON {database}.* TO {database}_rw@'192.168.%' WITH GRANT OPTION;".format(new_pwd=new_pwd, database=database)
            db_create_user = MySQL(dbconfig_db)
            db_create_user.query(sql_create_user)
            db_create_user.commit()
            create_user_info = db_create_user.fetchOneRow()
            db_create_user.close()

            print port
            print database
            print database + '_rw'
            print new_pwd
            print 'rw'


        create_database_info_list = []

        create_database_keys = ['port', 'database', 'user', 'password', 'grants']
        create_database_values = [port, database, database + '_rw', new_pwd, 'rw']

        create_database_keyvalue_info = dict(zip(create_database_keys, create_database_values))
        #print create_database_keyvalue_info
        create_database_info_list.append(create_database_keyvalue_info)


        #print json.dumps(audit_info_list)
        resp = Response(json.dumps(create_database_info_list))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        return resp



    except Exception, e:
        error_msg = "[action]:add database " \
                    "[status]:FAIL" \
                    "[Errorcode]:{e}".format(e=e)

        logger.error(error_msg)


