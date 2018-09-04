import datetime
import time
import json
from datetime import date


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def create_error(code=1, msg=''):
    return {"code": code, "msg": msg}


def create_success(msg):
    return {"code": 0, "msg": msg}


def gen_time_str():
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def print_time():
    print(gen_time_str())


def print_time_info(s):
    print("[%s] %s" % (gen_time_str(), s))


def make_response(data):
    from flask import make_response
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response
