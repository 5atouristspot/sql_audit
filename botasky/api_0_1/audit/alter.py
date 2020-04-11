#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Created on 2019-7-22


@module: audit
@used: audit sql
"""

from . import api
from flask import request, jsonify, Response
import json
from botasky.utils.MyCONN import MySQL

from botasky.utils.MyFILE import project_abdir, recursiveSearchFile
from botasky.utils.MyLOG import MyLog
logConfig = recursiveSearchFile(project_abdir, '*logConfig.ini')[0]
mylog = MyLog(logConfig, 'alter.py')
logger = mylog.outputLog()

import ConfigParser
config = ConfigParser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)



__all__ = ['alter']
__author__ = 'zhihao'

@api.route('/alter', methods=['GET', 'POST'])
def alter():
    '''
    :put in: port
    :put in: database
    :put in: sql_statment
    '''
    try:
        port = request.args.get('port', type=int, default=None)
        database = request.args.get('database', type=str, default='inception_test')
        sql_statment = request.args.get('sql_statment', type=unicode, default="alter TABLE user_dept_relation add content_html8 longtext COMMENT 'H5';")

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
        db.close()
        if result_info is not None:
            ip_info = result_info[0]
                #print ip_info
        else:
            ip_info = ''
            #print ip_info

        # --enable-check　--enable-execute
        sql_audit = "/*--user={user};--password={passwd};--host={ip_info};--enable-check;--port={port};*/" \
              "inception_magic_start;" \
              "use {database};" \
              "{sql_statment}" \
              "inception_magic_commit;".format(user=config.get('STRUCT', 'user'),passwd=config.get('STRUCT', 'pwd'), port=port, ip_info=ip_info, database=database, sql_statment=sql_statment.encode('utf-8'))

        print sql_audit
        inception_config = {'host': config.get('inception', 'host'),
                    'port': int(config.get('inception', 'port')),
                    'user': '',
                    'passwd': '',
                    'db': '',
                    'charset': 'utf8'}
        inception_db = MySQL(inception_config)
        inception_db.query(sql_audit)
        inception_db.commit()
        result_info = inception_db.fetchAllRows()
        #print result_info
        inception_db.close()

        audit_info_list = []

        audit_keys = ['ID', 'stage', 'errlevel', 'stagestatus', 'errormessage', 'SQL', 'Affected_rows', 'sequence', 'backup_dbname', 'execute_time', 'sqlsha1']
        for audit_info in result_info:
            audit_values = []
            for audit_value in audit_info:
                audit_values.append(audit_value)

            audit_keyvalue_info = dict(zip(audit_keys, audit_values))
            #print audit_keyvalue_info
            audit_info_list.append(audit_keyvalue_info)


        #print json.dumps(audit_info_list)
        resp = Response(json.dumps(audit_info_list))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        return resp



    except Exception, e:
        error_msg = "[action]:audit sql " \
                    "[status]:FAIL" \
                    "[Errorcode]:{e}".format(e=e)

        logger.error(error_msg)
