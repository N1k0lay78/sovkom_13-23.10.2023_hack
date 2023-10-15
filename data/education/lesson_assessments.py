import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class LessonAssessments(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'lesson-assessments'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    student_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("student.id"))
    student = orm.relationship('Student')

    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("group.id"))
    group = orm.relationship('Group')

    lesson_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("lesson.id"))
    lesson = orm.relationship('Lesson')

    visit = sqlalchemy.Column(sqlalchemy.Boolean, server_default='f', default=False)
    mark = sqlalchemy.Column(sqlalchemy.Integer)

    date = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), nullable=False)

    def __repr__(self):
        return f'<LessonAssessments> Оценка за занятие {self.id} {self.lesson.name} {self.student.name}'
