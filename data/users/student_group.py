import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class StudentGroup(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'student-group'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("group.id"))
    group = orm.relationship('group')

    student_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("student.id"))
    student = orm.relationship('student')

    start_education_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    end_education_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))
