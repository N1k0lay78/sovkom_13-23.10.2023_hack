import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class Academic(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'academic'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)
    user = orm.relationship('User', back_populates="academic")

    position = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    self_promotion = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'<Academic> Препод {self.user.id} {self.user.email} {self.user.name}'
