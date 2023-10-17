import datetime

from data import db_session
from data.education.lesson import Lesson
from data.users.academic import Academic
from data.users.curator import Curator
from data.users.group import Group
from data.users.student import Student

db_session.global_init("db/study.sqlite")

session = db_session.create_session()

students = [
    ["student@gmail.com", "admin123", "Студент Коля"],
    ["klimov200000@gmail.com", "admin123", "Студент Аня"],
]

for mail, passw, name in students:
    new_student = Student()
    new_student.email = mail
    new_student.set_password(passw)
    new_student.name = name

    session.add(new_student)
    session.commit()

academics = [
    ["academic@gmail.com", "admin123", "Академик Николай", "Профессор"],
]

for mail, passw, name, position in academics:
    new_academic = Academic()
    new_academic.email = mail
    new_academic.set_password(passw)
    new_academic.name = name
    new_academic.position = position

    session.add(new_academic)
    session.commit()

session.close()

curators = [
    ["curator@gmail.com", "admin123", "Куратор Николай Владимирович", "Курирует всё"],
]

for mail, passw, name, position in curators:
    new_curator = Curator()
    new_curator.email = mail
    new_curator.set_password(passw)
    new_curator.name = name
    new_curator.position = position

    session.add(new_curator)
    session.commit()

groups = [
    # name, description, curator_id, start_time, end_time, students
    ["программирование", "группа программистов", 4, datetime.datetime.strptime("13.10.2023", "%d.%m.%Y"),
     datetime.datetime.strptime("27.10.2023", "%d.%m.%Y"), [1,2]],
]

for name, desc, curator_id, start, end, stud_ids in groups:
    new_group = Group()
    new_group.name = name
    new_group.about = desc
    new_group.curator_id = curator_id
    new_group.start_education_time = start
    new_group.end_education_time = end

    for ind in stud_ids:
        new_group.students.append(session.query(Student).get(ind))

    session.add(new_group)
    session.commit()

lessons = [
    # name, description, academics, time [day 1-21, time HH:MM, count], groups
    ["программирование", "группа программистов", [3], [1, "14:00", 10], [1]],
]

for name, desc, academics_ids, time, stud_ids in lessons:
    new_lesson = Lesson()
    new_lesson.name = name
    new_lesson.about = desc
    new_lesson.day_week = time[0]
    new_lesson.time = time[1]
    new_lesson.count = time[2]

    for ind in academics_ids:
        new_lesson.academics.append(session.query(Academic).get(ind))

    for ind in stud_ids:
        new_lesson.groups.append(session.query(Group).get(ind))

    session.add(new_lesson)
    session.commit()

print(session.query(Lesson).get(1))

session.close()
