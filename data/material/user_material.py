
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class UserMaterial(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'user-material'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    user = orm.relationship('User')

    material_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("material.id"))
    material = orm.relationship('Material')
