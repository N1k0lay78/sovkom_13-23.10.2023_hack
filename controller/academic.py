from data import db_session
from data.users.academic import Academic
from data.users.user import User


def post_academic_info(academic_id, data):
    session = db_session.create_session()
    academic = session.query(Academic).get(academic_id)
    if not academic:
        session.close()
        return {"status": "error", "message": "преподаватель не существует"}

    for key, val in data.items():
        if key == "name":
            academic.name = val
        elif key == "ava":
            # TODO: сохранение картинки
            pass
        elif key == "email":
            if session.query(User).filter(User.email == val).first():
                session.close()
                return {"status": "error", "message": "пользователь с такой почтой уже существует"}
            academic.email = val
        elif key == "password":
            # TODO: сделать валидацию пароля
            academic.set_password(val)

    session.commit()
    session.close()
    return {"status": "ok", "message": "информация обновлена"}


def get_academic_info(academic_id):
    session = db_session.create_session()
    academic = session.query(Academic).get(academic_id)
    if not academic:
        session.close()
        return {"status": "error", "message": "преподаватель не существует"}
    # TODO: добавить получение успеваемости по предметам
    resp = {"status": "ok",
            "message": "",
            "data": {
                "name": academic.name,
                "ava": academic.ava,
                "email": academic.email,
                "position": academic.position,
                "self_promotion": academic.self_promotion,
                # "lessons": [{"name": lesson.name, "id": lesson.id} for lesson in academic.lessons],  #TODO: занятия
                "groups": [{"name": group.name, "id": group.id} for group in academic.groups],
            }}
    session.close()
    return resp


def get_lessons(academic_id):
    session = db_session.create_session()
    academic = session.query(Academic).get(academic_id)
    if not academic:
        session.close()
        return {"status": "error", "message": "Преподаватель не существует"}


    data = [[] for _ in range(7)]

    for classe in academic.classes:
        for lesson in classe.lessons:
            data[int(lesson.day_week - 1)].append({
                "time": ":".join(str(lesson.date.time()).split(":")[:-1]),
                "type_week": lesson.type_week,
                "name": lesson.classes.name,
                "description": lesson.classes.description,
                "academic_name": lesson.classes.academics[0].name,
                "auditory": lesson.auditory,
            })
    session.close()

    for i in range(7):
        data[i].sort(key=lambda x: x["time"])

    return {"status": "ok", "message": "", "data": data}


# def create_file(academic_id, data, file):
#     session = db_session.create_session()
#     academic = session.query(Academic).get(academic_id)
#     if not academic:
#         session.close()
#         return {"status": "error", "message": "преподаватель не существует"}
#
#     # TODO: сохранение файла
#
#     session.close()
#     return {"status": "ok",
#             "message": "файл создан",
#             "data": {
#                 "href": ""  # ссылка на файл
#             }}



