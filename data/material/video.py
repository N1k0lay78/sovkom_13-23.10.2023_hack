import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Video(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'video'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("material.id"), primary_key=True)
    material = orm.relationship('Material', back_populates="video")

    link = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)
    timecodes = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'<Video> Видео-конспект {self.material.id} {self.material.name}'
