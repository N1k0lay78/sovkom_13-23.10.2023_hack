import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Abstract(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'abstract'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("academic-material.id"), primary_key=True)
    material = orm.relationship('AcademicMaterial', back_populates="abstract")

    text = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        return f'<Abstract> Конспект {self.material.id} {self.material.href} {self.material.name}'
