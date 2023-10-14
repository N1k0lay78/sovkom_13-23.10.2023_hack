import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Student(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'student'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)
    user = orm.relationship('User', back_populates="student")
    name = sqlalchemy.Column(sqlalchemy.String)
    ava = sqlalchemy.Column(sqlalchemy.String)
    group_id = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self):
        return f'<Student> Студент {self.user.id} {self.user.email} {self.name}'
