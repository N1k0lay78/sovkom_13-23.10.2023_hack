import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Assessment(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'lesson-assessments'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    student_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("student.id"))
    student = orm.relationship('Student')

    lesson_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("lesson-day.id"))
    lesson = orm.relationship('LessonDay')

    material_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("edu-material.id"))
    material = orm.relationship('EduMaterial')

    visit = sqlalchemy.Column(sqlalchemy.Boolean, server_default='f', default=False)
    mark = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self):
        return f'<Assessments> {self.id}:{self.lesson.classes.name}:{self.student.name}'
