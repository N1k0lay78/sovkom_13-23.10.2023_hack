import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Presentation(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'presentation'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("academic-material.id"), primary_key=True)
    material = orm.relationship('AcademicMaterial', back_populates="presentation")

    link = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'<Presentation> Презентация-конспект {self.material.id} {self.material.href} {self.material.name}'
