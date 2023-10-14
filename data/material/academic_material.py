import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class AcademicMaterial(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'academic-material'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    academic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("academic.id"))
    academic = orm.relationship('Academic')

    href = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    ava = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    video = orm.relationship('Video', back_populates="material")
    presentation = orm.relationship('Presentation', back_populates="material")
    abstract = orm.relationship('Abstract', back_populates="material")

    def __repr__(self):
        return f'<Academic-Material> Академик-Материал {self.id} {self.academic.name} {self.href}'
