from datetime import datetime

from controller.file import create_empty_file
from data.education.lesson import Сlasses, LessonDay
from data.education.assessments import Assessment
from data import db_session
from data.material.edu_material import EduMaterial
from data.users.academic import Academic
from data.users.group import Group


def create_classes(name, academ_email, count_lessons, desc=""):
    session = db_session.create_session()

    new_classes = Сlasses()
    new_classes.name = name
    new_classes.description = desc

    academic = session.query(Academic).filter(Academic.email == academ_email).first()

    if not academic:
        session.close()
        return {"status": "error", "message": "преподаватель не существует"}

    new_classes.academics.append(academic)

    session.add(new_classes)
    session.commit()

    for _ in range(count_lessons):
        new_lesson = LessonDay()
        new_lesson.type_week = 2

        # date = "01.01.2023 00:00"
        date_str = f'2023-01-1 14:30'
        date_format = '%Y-%m-%d %H:%M'
        date_obj = datetime.strptime(date_str, date_format)

        new_lesson.date = date_obj
        new_lesson.day_week = date_obj.weekday()+1
        new_lesson.auditory = ""
        new_lesson.text_hw = "Задания нету"
        new_lesson.classes = new_classes

        session.add(new_lesson)
        session.commit()

    session.close()
    return {"status": "ok", "message": "занятие создано"}


def get_all_classes():
    session = db_session.create_session()

    classes = session.query(Сlasses).all()

    data = []
    week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    for classe in classes:
        data.append([classe.name, [[week[int(lesson.day_week) - 1], lesson.auditory, "Будет" if lesson.public else "План", lesson.text_hw] for lesson in classe.lessons]])

    session.close()
    return {"status": "ok", "message": "", "data": data}


def classes_add_group(classes_id, group_id):
    session = db_session.create_session()

    classes = session.query(Сlasses).get(classes_id)

    if not classes:
        session.close()
        return {"status": "error", "message": "занятие не существует"}

    group = session.query(Group).filter(Group.name == group_id).first()

    if not group:
        session.close()
        return {"status": "error", "message": "группа не существует"}

    classes.groups = [group]
    session.add(classes)
    session.commit()

    session.close()

    update_assessments(classes_id)

    return {"status": "ok", "message": "занятие создано"}


def create_assessment(stud, lesson, session):
    new_assessment = Assessment()
    new_assessment.student = stud
    new_assessment.lesson = lesson
    new_assessment.material = session.query(EduMaterial).get(create_empty_file(session)["id"])

    session.add(new_assessment)


def update_assessments(classes_id):
    session = db_session.create_session()

    classes = session.query(Сlasses).get(classes_id)

    if not classes:
        session.close()
        return {"status": "error", "message": "занятие не существует"}

    if not classes.groups:
        session.close()
        return {"status": "error", "message": "к занятию нету прикреплённых групп"}

    group = classes.groups[0]

    for lesson in classes.lessons:
        for stud in group.students:
            assessment = session.query(Assessment).filter(Assessment.student_id == stud.id, Assessment.lesson_id == lesson.id).first()
            if not assessment:
                create_assessment(stud, lesson, session)

    session.close()
    return {"status": "ok", "message": "оценки обновлены"}


def edit_lesson(id, type_week, date, auditory, text_hw, public):
    session = db_session.create_session()

    lesson = session.query(LessonDay).get(id)

    lesson.type_week = type_week

    date_format = '%Y-%m-%d %H:%M'
    date_obj = datetime.strptime(date, date_format)
    lesson.date = date_obj
    lesson.day_week = date_obj.weekday()+1

    lesson.auditory = auditory
    lesson.text_hw = text_hw
    lesson.public = public

    session.add(lesson)
    session.commit()

    session.close()
