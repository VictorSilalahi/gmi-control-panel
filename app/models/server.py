from ..utils.db import db
from sqlalchemy.sql import func

class Server(db.Model):
    __tablename__ = "tserver"
    server_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.String(50))
    nama_gereja = db.Column(db.String(100))

    def __init__(self, link, nama_gereja):
        self.link = link
        self.nama_gereja = nama_gereja

    def json(self):
        return {
            "server_id": self.server_id,
            "link": self.link,
            "nama_gereja": self.nama_gereja
        }
