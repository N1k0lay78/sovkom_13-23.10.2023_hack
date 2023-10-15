import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy.sql import func


class MaterialAccessGroup(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'material-access-group'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("group.id"))
    group = orm.relationship('Group')

    material_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("material.id"))
    material = orm.relationship('Material')

    access_time = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<MaterialAccessGroup> Доступ для группы к материалу {self.id} {self.material.name} {self.group.name}'
