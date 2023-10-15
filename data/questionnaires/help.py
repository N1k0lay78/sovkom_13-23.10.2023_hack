import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class QuestionnairesHelp(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'questionnaires-help'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
