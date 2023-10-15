import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class Group(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'group'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    about = sqlalchemy.Column(sqlalchemy.String)
    time_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    curator_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("curator.id"))
    curator = orm.relationship('curator')
