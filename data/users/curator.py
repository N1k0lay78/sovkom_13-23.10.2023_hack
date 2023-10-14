import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Curator(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'curator'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)
    user = orm.relationship('User', back_populates="curator")
    name = sqlalchemy.Column(sqlalchemy.String)
    ava = sqlalchemy.Column(sqlalchemy.String)
    position = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'<Curator> Проф ком {self.user.id} {self.user.email} {self.name}'
