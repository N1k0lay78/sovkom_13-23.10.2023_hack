import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class File(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'file'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    href = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    link = sqlalchemy.Column(sqlalchemy.String)

    academic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("academic.id"))
    academic = orm.relationship('Academic')

    time_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    time_edited = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f'<File> файл {self.id} {self.academic.name} {self.link}'
