from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import get_core_app
from helpers import hash_password, verify_password
from settings import DB_NAME, DB_PATH

app = get_core_app()
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'{self.username}: {self.name}'

    def set_password(self, password):
        self.password = hash_password(password)

    def check_password(self, password):
        return verify_password(self.password, password)


class UserToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, ForeignKey(User.id))

    user = relationship('User', foreign_keys='UserToken.user_id')

    def __repr__(self):
        return f'{self.id} {self.token}'


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(50))
    result = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey(User.id))

    user = relationship('User', foreign_keys='Report.user_id')