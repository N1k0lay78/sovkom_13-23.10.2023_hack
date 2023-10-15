import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class StudentCertificate(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'student-certificate'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    student_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("student.id"))
    student = orm.relationship('Student')

    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    link = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    description = sqlalchemy.Column(sqlalchemy.String)
    comment = sqlalchemy.Column(sqlalchemy.String)
    getting_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<StudentCertificate> Сертификат студента {self.id} {self.name} {self.student.name}'

