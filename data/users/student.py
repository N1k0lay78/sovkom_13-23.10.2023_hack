import sqlalchemy
from sqlalchemy import orm

from data.education.event import student_event
from data.users.group import student_group
from data.users.user import User


class Student(User):
    __tablename__ = 'student'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)

    groups = orm.relationship("Group", secondary=student_group)
    events = orm.relationship("Event", secondary=student_event)

    is_end_education = sqlalchemy.Column(sqlalchemy.Boolean, default=False, nullable=False, server_default='f')

    def __repr__(self):
        return f'<Student> Студент {self.id} {self.email} {self.name}'
