import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class Message(SqlAlchemyBase):
    __tablename__ = 'message'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    send_user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    recv_user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))

    message = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    time_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    read = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, server_default="f", default=False)

    def __repr__(self):
        return f'<Message> Сообщение {self.id} {self.send_user_id} {self.recv_user_id}'
