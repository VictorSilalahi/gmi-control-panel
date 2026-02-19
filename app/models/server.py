from ..utils.db import db
from sqlalchemy.sql import func

class Server(db.Model):
    __tablename__ = "tjabatan"
    jabatan_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jabatan = db.Column(db.String(50))

    def __init__(self, jabatan):
        self.jabatan = jabatan

    def json(self):
        return {
            "jabatan_id": self.jabatan_id,
            "jabatan": self.jabatan
        }
