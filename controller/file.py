import os

from werkzeug.utils import secure_filename

from data import db_session
from data.material.edu_material import EduMaterial
from data.message.message import Message
from data.users.user import User
from main import uploads_dir


def get_file_info(id):
    session = db_session.create_session()

    material = session.query(EduMaterial).get(id)

    if not material:
        session.close()
        return {"status": "error", "message": "файл не существует", "data": {"name": "", "href": ""}}

    href = material.href
    name = material.name

    session.close()
    return {"status": "ok", "message": "", "data": {"name": name, "href": href}}


def get_file_path(href):
    session = db_session.create_session()

    material = session.query(EduMaterial).filter(EduMaterial.href == href).first()

    if not material:
        session.close()
        return {"status": "error", "message": "файл не существует", "filename": ""}

    filename = material.filename

    session.close()
    return {"status": "ok", "message": "", "filename": filename}


def create(href, name, file, type):
    session = db_session.create_session()

    new_material = EduMaterial()
    new_material.href = href
    new_material.name = name
    new_material.type = type
    filename = secure_filename(file.filename)
    new_material.filename = filename

    file.save(os.path.join(uploads_dir, filename))

    session.add(new_material)
    session.commit()

    session.close()
    return {"status": "ok", "message": ""}
