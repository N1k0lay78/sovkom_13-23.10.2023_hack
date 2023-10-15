import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class MaterialAccessUser(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'material-access-user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    user = orm.relationship('User')

    material_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("material.id"))
    material = orm.relationship('Material')

    access_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<MaterialAccessUser> Доступ для пользователя к материалу {self.id} {self.material.name} {self.user.name}'
