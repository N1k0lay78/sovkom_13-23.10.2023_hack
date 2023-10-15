import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class Student(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'student'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)
    user = orm.relationship('User', back_populates="student")

    is_end_education = sqlalchemy.Column(sqlalchemy.Boolean, default=False, nullable=False, server_default='f')

    def __repr__(self):
        return f'<Student> Студент {self.user.id} {self.user.email} {self.user.name}'
