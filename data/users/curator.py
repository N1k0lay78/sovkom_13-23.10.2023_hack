import sqlalchemy
from data.users.user import User


class Curator(User):
    __tablename__ = 'curator'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"), primary_key=True)

    position = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        return f'<Curator> Проф ком {self.id} {self.email} {self.name}'
