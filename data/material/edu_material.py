import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class EduMaterial(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'edu-material'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    href = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    filename = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    time_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    time_edited = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f'<EduMaterial> Материал для обучения {self.id} {self.name}'
