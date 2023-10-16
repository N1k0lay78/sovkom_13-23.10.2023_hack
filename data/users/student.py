import sqlalchemy
from data.users.user import User


class Student(User):
    __tablename__ = 'student'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)

    is_end_education = sqlalchemy.Column(sqlalchemy.Boolean, default=False, nullable=False, server_default='f')

    def __repr__(self):
        return f'<Student> Студент {self.id} {self.email} {self.name}'
