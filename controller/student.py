from data import db_session
from data.users.group import Group
from data.users.student import Student
from data.users.user import User


def get_lesson_of_user(user_id):
    session = db_session.create_session()
    stud = session.query(Student).get(user_id)
    if not stud:
        session.close()
        return {"status": "error", "message": "студент не существует"}
    if not stud.groups:
        session.close()
        return {"status": "error", "message": "студент не состоит в группе"}
    group_id = stud.groups[0].id
    session.close()
    return get_lessons(group_id)


def get_lessons(group_id):
    session = db_session.create_session()
    group = session.query(Group).get(group_id)
    if not group:
        session.close()
        return {"status": "error", "message": "группа не существует"}
    lessons = group.lessons
    if not lessons:
        session.close()
        return {"status": "ok", "message": "занятий нет", "data": {}}
    data = [[] for _ in range(7)]
    for lesson in lessons:
        data[int(lesson.day_week - lesson.day_week // 7 * 7)].append({
            "time": lesson.time,
            "type_week": lesson.day_week // 7,
            "name": lesson.name,
            "description": lesson.description,
            "academic_name": lesson.academics[0].name,
            "auditory": lesson.auditory,
        })
    session.close()
    for i in range(7):
        data[i].sort(key=lambda x: x["time"])
    return {"status": "ok", "message": "", "data": data}


def post_student_info(student_id, data):
    session = db_session.create_session()
    student = session.query(Student).get(student_id)
    if not student:
        session.close()
        return {"status": "error", "message": "студент не существует"}

    for key, val in data.items():
        if key == "name":
            student.name = val
        elif key == "ava":
            # TODO: сохранение картинки
            pass
        elif key == "email":
            if session.query(User).filter(User.email == val).first():
                session.close()
                return {"status": "error", "message": "пользователь с такой почтой уже существует"}
            student.email = val
        elif key == "password":
            #TODO: сделать валидацию пароля
            student.set_password(val)
        elif key == "group":
            group = session.query(Group).get(val)
            if not group:
                session.close()
                return {"status": "error", "message": "группа не существует"}
            student.groups = [group]
        elif key == "is_education":
            student.is_end_education = not val

    session.commit()
    session.close()
    return {"status": "ok", "message": "информация обновлена"}


def get_student_info(student_id):
    session = db_session.create_session()
    student = session.query(Student).get(student_id)
    if not student:
        session.close()
        return {"status": "error", "message": "студент не существует"}
    # TODO: добавить получение успеваемости по предметам
    resp = {"status": "ok",
            "message": "",
            "data": {
                "name": student.name,
                "group": student.groups[0],
                "ava": student.ava,
                "is_education": not student.is_end_education,
                "email": student.email,
                #TODO: занятия
            }}
    session.close()
    return resp