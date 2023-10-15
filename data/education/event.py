import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Event(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'event'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    ava = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)

    start_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), nullable=False)
    duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __repr__(self):
        return f'<Event> Мероприятие {self.id} {self.name}'
