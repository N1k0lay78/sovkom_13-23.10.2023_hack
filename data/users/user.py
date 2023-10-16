import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    time_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ava = sqlalchemy.Column(sqlalchemy.String)

    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "employee",
        "polymorphic_on": "type",
    }

    def __repr__(self):
        return f'<User> Пользователь {self.id} {self.email}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
