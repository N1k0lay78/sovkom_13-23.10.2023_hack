import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Comment(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'comment'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    material_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("material.id"))
    material = orm.relationship('Material')

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    user = orm.relationship('User')

    comment = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        return f'<Comment> Комментарий {self.id} {self.material.name} {self.user.name}'
