import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class LessonDay(SqlAlchemyBase):
    __tablename__ = 'lesson-day'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    type_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # day from 0 to 2
    day_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # day from 1 to 7
    date = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))
    auditory = sqlalchemy.Column(sqlalchemy.String)
    public = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, server_default='t', default=True)
    # homework = sqlalchemy.Column(sqlalchemy.String)

    text_hw = sqlalchemy.Column(sqlalchemy.String)

    classes_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("classes.id"))
    classes = orm.relationship("Сlasses")
    assessments = orm.relationship("Assessment")

    def __repr__(self):
        return f'<LessonDay> Урок {self.id} '


group_lesson = sqlalchemy.Table(
    'group-classes', SqlAlchemyBase.metadata,
    sqlalchemy.Column('group_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('group.id')),
    sqlalchemy.Column('classes_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('classes.id'))
)

academic_lesson = sqlalchemy.Table(
    'academic-classes', SqlAlchemyBase.metadata,
    sqlalchemy.Column('classes_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('classes.id')),
    sqlalchemy.Column('academic_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('academic.id')),
)


class Сlasses(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'classes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    ava = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)

    # day_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # day from 1 to 21 (2 week up and down and all weeks)
    # time = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # HH:MM
    # auditory = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    # count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    # constant duration

    academics = orm.relationship("Academic", secondary=academic_lesson)
    groups = orm.relationship("Group", secondary=group_lesson)
    lessons = orm.relationship("LessonDay")

    def __repr__(self):
        return f'<Сlasses> Занятие {self.id} {self.name} {self.academics}:{self.groups}'


# group_lesson = sqlalchemy.Table(
#     'group-lesson', SqlAlchemyBase.metadata,
#     sqlalchemy.Column('group_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('group.id')),
#     sqlalchemy.Column('lesson_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('lesson.id'))
# )
#
# academic_lesson = sqlalchemy.Table(
#     'academic-lesson', SqlAlchemyBase.metadata,
#     sqlalchemy.Column('lesson_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('lesson.id')),
#     sqlalchemy.Column('academic_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('academic.id')),
# )
#
# class Lesson(SqlAlchemyBase, UserMixin, SerializerMixin):
#     __tablename__ = 'lesson'
#     id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
#
#     ava = sqlalchemy.Column(sqlalchemy.String)
#     name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
#     description = sqlalchemy.Column(sqlalchemy.String)
#
#     day_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # day from 1 to 21 (2 week up and down and all weeks)
#     time = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # HH:MM
#     auditory = sqlalchemy.Column(sqlalchemy.String, nullable=False)
#     count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
#     # constant duration
#
#     academics = orm.relationship("Academic", secondary=academic_lesson)
#     groups = orm.relationship("Group", secondary=group_lesson)
#     assessments = orm.relationship("Assessment")
#
#     def __repr__(self):
#         return f'<Lesson> Занятие {self.id} {self.name} {self.academics}:{self.groups}:{self.assessments}'