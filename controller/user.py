from data import db_session
from data.users.group import Group
from data.users.student import Student


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
                "email": student.email
            }}
    session.close()
    return resp