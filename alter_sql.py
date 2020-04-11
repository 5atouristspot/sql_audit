#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import requests
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", help="audit sql",
                        action="store_true")
    parser.add_argument("--execute", help="execute sql",
                        action="store_true")
    parser.add_argument('-P', type=str, help="port of instance", default='4450')
    parser.add_argument('-d', type=str, help="database", default='test')
    parser.add_argument('-s', type=str, help="sql statment", default=u"alter table view_2018 add view_type2 tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '哈哈' after mark;")

    args = parser.parse_args()

    return args

def test_audit_alter_ok(port, database, sql_statment):
    arg = get_arg()

    #sql_statment = unicode(sql_statment, 'utf8')
    #sql_statment = sql_statment.encode('ascii', 'replace')
    #sql_statment = sql_statment.encode('ascii')

    ok_request = requests.get(url='http://10.20.1.146:3621/api/v1000/audit/alter',
                              params={'port': '{port}'.format(port=port), 'database': '{database}'.format(database=database), 'sql_statment': "{sql_statment}".format(sql_statment=sql_statment)})
    print(ok_request.url)
    #print(ok_request.status_code)
    text_info = eval(ok_request.text)
    print "返回json:"
    print(text_info)

    if(200 == ok_request.status_code):
        print 'status_code is OK'.format(database=arg.d)
    else:
        print 'status_code is {code}}'.format(code=ok_request.status_code)
    if (0 == text_info[0]['errlevel']):
        print 'use {database} is OK '.format(database=arg.d)
    else:
        print 'use {database} is FAIL '.format(database=arg.d)
    if(0==text_info[1]['errlevel']):
        print '{sql_statment} is OK '.format(sql_statment=arg.s)
    else:
        print '{sql_statment} is FAIL '.format(sql_statment=arg.s)
        print text_info[1]['errormessage']


def test_execute_alter_ok(port, database, sql_statment):
    arg = get_arg()

    #sql_statment = unicode(sql_statment, 'utf8')
    #sql_statment = sql_statment.encode('ascii', 'replace')

    ok_request = requests.get(url='http://10.20.1.146:3621/api/v1000/execute/alter',
                              params={'port': '{port}'.format(port=port), 'database': '{database}'.format(database=database), 'sql_statment': "{sql_statment}".format(sql_statment=sql_statment)})
    #print(ok_request.url)
    #print(ok_request.status_code)
    text_info = eval(ok_request.text)
    print "返回json:"
    print(text_info)

    if(200 == ok_request.status_code):
        print 'status_code is OK'.format(database=arg.d)
    else:
        print 'status_code is {code}}'.format(code=ok_request.status_code)
    if (0 == text_info[0]['errlevel']):
        print 'use {database} is OK '.format(database=arg.d)
    else:
        print 'use {database} is FAIL '.format(database=arg.d)
    if(0==text_info[1]['errlevel']):
        print '{sql_statment} is OK '.format(sql_statment=arg.s)
    else:
        print '{sql_statment} is FAIL '.format(sql_statment=arg.s)
        print text_info[1]['errormessage']


def main():
    arg = get_arg()
    if arg.audit:
        test_audit_alter_ok(arg.P, arg.d, arg.s)
    elif arg.execute:
        test_execute_alter_ok(arg.P, arg.d, arg.s)

if __name__ == '__main__':
    main()

