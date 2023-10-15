import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class QuestionnairesJoin(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'questionnaires-join'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)