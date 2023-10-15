import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class EventLeading(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'event-leading'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    user = orm.relationship('User')

    event_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("event.id"))
    event = orm.relationship('Event')

    time_join = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<EventLeading> Ведущий мероприятия {self.id} {self.event.name} {self.user.name}'
