#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Created on 2017-7-04
Modify on 2017-12-01


@module: run
@used: main of botasky
"""

import os
from flask import Flask

from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

from botasky.utils.MyDAEMON import daemonize

__all__ = ['create_app', 'main']
__author__ = 'zhihao'


#used of running gunicorn

#apt-get install figlet
#os.system('figlet botasky')

app = Flask(__name__)

from api_0_1 import api as api_1_0_blueprint
app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1000')

from api_0_1.audit import api as api_1_0_audit_blueprint
app.register_blueprint(api_1_0_audit_blueprint, url_prefix='/api/v1000/audit')

from api_0_1.execute import api as api_1_0_execute_blueprint
app.register_blueprint(api_1_0_execute_blueprint, url_prefix='/api/v1000/execute')

from api_0_1.add import api as api_1_0_add_blueprint
app.register_blueprint(api_1_0_add_blueprint, url_prefix='/api/v1000/add')

def create_app():
    app = Flask(__name__)

    from api_0_1.audit import api as api_1_0_audit_blueprint
    app.register_blueprint(api_1_0_audit_blueprint, url_prefix='/api/v1000/audit')

    from api_0_1.execute import api as api_1_0_execute_blueprint
    app.register_blueprint(api_1_0_execute_blueprint, url_prefix='/api/v1000/execute')

    return app


def main():
    #apt-get install figlet
    os.system('figlet botasky')

    daemonize('/dev/null', '/tmp/botasky_stdout.log', '/tmp/botasky_stdout.log')

    app = create_app()

    server = WSGIServer(('10.20.4.47', 3621), app)
    server.serve_forever()



if __name__ == '__main__':
    #curl -u da:xinxin -i -X GET http://192.168.41.12:3621/api/v1000/
    app.run(debug=False, host='192.168.74.95', port=3621)
