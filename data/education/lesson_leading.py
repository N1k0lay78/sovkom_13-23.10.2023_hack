import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class LessonLeading(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'lesson-leading'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    academic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("academic.id"))
    academic = orm.relationship('Academic')

    lesson_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("lesson.id"))
    lesson = orm.relationship('Lesson')

    time_join = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<LessonLeading> Препод занятия {self.id} {self.lesson.name} {self.academic.name}'
