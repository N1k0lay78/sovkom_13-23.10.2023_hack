import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase

group_lesson = sqlalchemy.Table(
    'group-lesson', SqlAlchemyBase.metadata,
    sqlalchemy.Column('group_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('group.id')),
    sqlalchemy.Column('lesson_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('lesson.id'))
)

academic_lesson = sqlalchemy.Table(
    'academic-lesson', SqlAlchemyBase.metadata,
    sqlalchemy.Column('lesson_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('lesson.id')),
    sqlalchemy.Column('academic_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('academic.id')),
)


class LessonDay(SqlAlchemyBase):
    __tablename__ = 'lesson-day'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    type_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # day from 1 to 3
    day_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # day from 1 to 7
    auditory = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    text_hw = sqlalchemy.Column(sqlalchemy.String)
    assessments = orm.relationship("Assessment")


class LessonName(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'lesson-name'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    ava = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)

    # day_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # day from 1 to 21 (2 week up and down and all weeks)
    # time = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # HH:MM
    # auditory = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    # constant duration

    academics = orm.relationship("Academic", secondary=academic_lesson)
    groups = orm.relationship("Group", secondary=group_lesson)

    def __repr__(self):
        return f'<Lesson-name> Название-занятия {self.id} {self.name} {self.academics}:{self.groups}'
