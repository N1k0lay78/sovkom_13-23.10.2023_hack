import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.sql import func
from data.db_session import SqlAlchemyBase
from data.education.lesson import group_lesson

student_group = sqlalchemy.Table(
    'student-group', SqlAlchemyBase.metadata,
    sqlalchemy.Column('student_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('student.id')),
    sqlalchemy.Column('group_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('group.id'))
)


class Group(SqlAlchemyBase):
    __tablename__ = 'group'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    about = sqlalchemy.Column(sqlalchemy.String)
    time_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    lessons = orm.relationship("Lesson", secondary=group_lesson)
    students = orm.relationship("Student", secondary=student_group)

    curator_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("curator.id"))
    curator = orm.relationship('Curator')

    start_education_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))
    end_education_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))

    def __repr__(self):
        return f'<Group> Группа {self.id} {self.name} {self.students}'
