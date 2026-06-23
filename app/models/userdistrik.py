from ..utils.db import db
from sqlalchemy.sql import func

class Userdistrik(db.Model):
    __tablename__ = "tuserdistrik"
    userdistrik_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    distrik = db.Column(db.String(50))

    def __init__(self, username, password, distrik):
        self.username = username
        self.password = password
        self.distrik = distrik

    def json(self):
        return {
            "userdistrik_id": self.userdistrik_id,
            "username": self.username,
            "password": self.password,
            "distrik": self.distrik
        }
