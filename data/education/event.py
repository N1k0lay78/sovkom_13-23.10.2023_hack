import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase

student_event = sqlalchemy.Table(
    'student-event', SqlAlchemyBase.metadata,
    sqlalchemy.Column('student_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('student.id')),
    sqlalchemy.Column('event_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('event.id'))
)

academic_event = sqlalchemy.Table(
    'academic-event', SqlAlchemyBase.metadata,
    sqlalchemy.Column('event_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('event.id')),
    sqlalchemy.Column('academic_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('academic.id')),
)


class Event(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'event'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    ava = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)

    start_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), nullable=False)
    duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    academics = orm.relationship("Academic", secondary=academic_event)
    students = orm.relationship("Student", secondary=student_event)

    def __repr__(self):
        return f'<Event> Мероприятие {self.id} {self.name} {self.academics}:{self.students}'
