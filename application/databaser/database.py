#  -*- coding:utf-8 -*-

from application import app

from pymongo import MongoClient

connection = MongoClient('mongodb://%s:%s@%s:%s/' % (
    app.config["DATABASE_USER"], app.config["DATABASE_PASS"], app.config["DATABASE_IP"], app.config["DATABASE_PORT"]))
db = connection.label
user_db = db.user
