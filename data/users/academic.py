import sqlalchemy
from data.users.user import User


class Academic(User):
    __tablename__ = 'academic'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)

    position = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    self_promotion = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'<Academic> Препод {self.id} {self.email} {self.name}'
