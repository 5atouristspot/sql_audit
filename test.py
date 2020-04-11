#!./venv/bin/python2.7
#-\*-coding: utf-8-\*-
import MySQLdb



sql="/*--user=djyv4_rw;--password=tfkj_secret;--host=10.20.4.44;--enable-check;--port=4450;*/" \
    "inception_magic_start;" \
    "use inception_test;" \
    "alter TABLE `user_dept_relation` add `content_html6` longtext COMMENT '�~F~E容H5';" \
    "inception_magic_commit;"

'''
sql = "/*--user=djyv4_rw;--password=tfkj_secret;--host=10.20.4.44;--enable-check;--port=4450;*/inception_magic_start;use inception_test;alterinception_magic_commit;"
'''
try:
    conn=MySQLdb.connect(host='10.20.1.171',user='',passwd='',db='',port=6669)
    cur=conn.cursor()
    ret=cur.execute(sql)
    result=cur.fetchall()
    num_fields = len(cur.description)
    field_names = [i[0] for i in cur.description]
    print field_names
    print result
    for row in result:
        print row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10]
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
