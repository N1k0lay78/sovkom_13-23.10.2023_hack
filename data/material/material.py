import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class Material(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'material'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    href = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    ava = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    # 0 - черновик, 1 - ограниченный доступ, 2 - открытый доступ
    status = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    time_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    time_edited = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), onupdate=func.now())

    video = orm.relationship('Video', back_populates="material")
    presentation = orm.relationship('Presentation', back_populates="material")
    abstract = orm.relationship('Abstract', back_populates="material")

    def __repr__(self):
        return f'<Material> Материал {self.id} {self.name}'
