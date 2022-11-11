from datetime import datetime
from . import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model, UserMixin):
    __tablename__: str = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(94), nullable=False)

    def __str__(self):
        return self.username

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def create_user(cls, username, email, password):
        user = User(username = username, email = email, password = generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get_by_id(cls, id):
        return User.query.filter_by(username=id).first()

    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return User.query.filter_by(email=email).first()

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String( 50 ), nullable = False)
    description = db.Column(db.Text())
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.Date, default = datetime.now())
