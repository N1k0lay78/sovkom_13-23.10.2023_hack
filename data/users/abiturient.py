import sqlalchemy
from data.users.user import User


class Abiturient(User):
    __tablename__ = 'abiturient'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)

    birthday = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))
    phone = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    social = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    direction = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    # other_email = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    time_job = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    achievements = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    motivation_message = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    accept = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, server_default='f', default=False)

    __mapper_args__ = {
        "polymorphic_identity": "abiturient",
    }

    def __repr__(self):
        return f'<Student> Студент {self.id} {self.email} {self.name}'
