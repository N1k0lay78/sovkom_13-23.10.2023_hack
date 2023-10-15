import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Lesson(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'lesson'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    ava = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)

    day_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # day from 1 to 14 (2 week up and down)
    time = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # HH:MM
    # constant duration

    def __repr__(self):
        return f'<Lesson> Занятие {self.id} {self.name}'
