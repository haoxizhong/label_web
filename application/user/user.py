from application.databaser import user_db

from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, username):
        super(User, self).__init__()

        self.username = username

    def get_id(self):
        return self.username


def insert_user(userid, password):
    user_db.insert({"userid": userid, "password": password, "name": ""})


def update_user(userid, username):
    user_db.update({"userid": userid}, {"$set": {"name": username}})


def check_user(userid, password):
    for res in user_db.find({"userid": userid}):
        if res["password"] != password:
            return False
    return True


def exist_user(userid):
    for res in user_db.find({"userid": userid}):
        return True
    return False


def find_user(userid):
    for res in user_db.find({"userid": userid}):
        res.pop("password")
        return res
    return None
