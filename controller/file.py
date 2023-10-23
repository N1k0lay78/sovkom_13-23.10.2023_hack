import os

from werkzeug.utils import secure_filename

from config import uploads_dir
from data import db_session
from data.material.edu_material import EduMaterial
from data.message.message import Message
from data.users.user import User
import random
import string


def get_files(file_type):
    session = db_session.create_session()

    materials = session.query(EduMaterial).order_by(-EduMaterial.id).all()

    if not materials:
        session.close()
        return {"status": "ok", "message": "файлов нет", "data": []}

    files = []
    for material in materials:
        href = material.href
        name = material.name
        id = material.id
        if material.type == file_type:
            files.append([href, name, id])

    if not files:
        session.close()
        return {"status": "ok", "message": "файлов нет", "data": []}

    session.close()
    return {"status": "ok", "message": "", "data": files}


def get_file_info(id):
    session = db_session.create_session()

    material = session.query(EduMaterial).get(id)

    if not material:
        session.close()
        return {"status": "error", "message": "файл не существует", "data": {"name": "", "href": "", "type": "", "id": 0}}

    href = material.href
    name = material.name
    type = material.type
    id = material.id

    session.close()
    return {"status": "ok", "message": "", "data": {"name": name, "href": href, "type": type, "id": id}}


def get_file_path(href):
    session = db_session.create_session()

    material = session.query(EduMaterial).filter(EduMaterial.href == href).first()

    if not material:
        session.close()
        return {"status": "error", "message": "файл не существует", "filename": ""}

    filename = material.filename

    session.close()
    return {"status": "ok", "message": "", "filename": filename}


def edit_file(id, name, href):
    session = db_session.create_session()

    material = session.query(EduMaterial).get(id)

    if not material:
        session.close()
        return {"status": "error", "message": "файл не существует"}

    fded = session.query(EduMaterial).filter(EduMaterial.href == href).first()

    if fded and fded != material:
        session.close()
        return {"status": "error", "message": "файл с такой ссылкой уже существует"}

    material.name = name
    material.href = href
    session.add(material)
    session.commit()

    session.close()
    return {"status": "ok", "message": "файл обновлён"}


def delete_file(id):
    session = db_session.create_session()

    material = session.query(EduMaterial).get(id)

    if not material:
        session.close()
        return {"status": "error", "message": "файл не существует"}

    os.remove(os.path.join(uploads_dir, material.filename))
    session.delete(material)
    session.commit()

    session.close()
    return {"status": "ok", "message": "файл удалён"}


def create_file(name, file, type):
    session = db_session.create_session()

    new_material = EduMaterial()
    new_material.name = name
    new_material.type = type
    letters = string.ascii_lowercase + "0123456789"
    filename = ''.join(random.choice(letters) for i in range(16))
    while filename + "." + file.filename.split(".")[-1] in os.listdir(uploads_dir):
        filename = ''.join(random.choice(letters) for i in range(16))
    print(filename)
    new_material.href = filename
    filename = filename + "." + file.filename.split(".")[-1]
    new_material.filename = filename

    file.save(os.path.join(uploads_dir, filename))

    session.add(new_material)
    session.commit()

    session.close()
    return {"status": "ok", "message": ""}
