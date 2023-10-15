import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class LessonMember(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'lesson-member'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("group.id"))
    group = orm.relationship('Group')

    lesson_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("lesson.id"))
    lesson = orm.relationship('Lesson')

    time_join = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<LessonMember> Участник занятия {self.id} {self.lesson.name} {self.group.name}'
