from .database import db
from sqlalchemy import Integer, String, TIMESTAMP


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(Integer, primary_key = True)
    username = db.Column(String(100), unique = True, nullable = False)
    password_hash = db.Column(String(255), nullable = False)
    created_at = db.Column(TIMESTAMP, server_default = db.func.now())

    def __repr__(self):
        return f"User(username = '{self.username}')"