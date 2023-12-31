import datetime

from controller.lessons import create_classes, classes_add_group
from data import db_session
from data.education.assessments import Assessment
from data.education.event import Event
from data.education.lesson import Сlasses, LessonDay
from data.users.abiturient import Abiturient
from data.users.academic import Academic
from data.users.curator import Curator
from data.users.group import Group
from data.users.student import Student

db_session.global_init("db/study.sqlite")

session = db_session.create_session()

students = [
    ["student@gmail.com", "admin123", ["toropov", "Коля", "vladimirovich"]],
    ["klimov200000@gmail.com", "admin123", ["toropov", "Коля", "vladimirovich"]],
]

for mail, passw, name in students:
    new_student = Student()
    new_student.email = mail
    new_student.set_password(passw)
    new_student.surname = name[0]
    new_student.name = name[1]
    new_student.family = name[2]

    session.add(new_student)
    session.commit()

academics = [
    ["academic@gmail.com", "admin123", ["toropov", "Коля", "vladimirovich"], "Профессор"],
]

for mail, passw, name, position in academics:
    new_academic = Academic()
    new_academic.email = mail
    new_academic.set_password(passw)
    new_academic.surname = name[0]
    new_academic.name = name[1]
    new_academic.family = name[2]
    new_academic.position = position

    session.add(new_academic)
    session.commit()

session.close()

curators = [
    ["curator@gmail.com", "admin123", ["toropov", "Коля", "vladimirovich"], "Курирует всё"],
]

for mail, passw, name, position in curators:
    new_curator = Curator()
    new_curator.email = mail
    new_curator.set_password(passw)
    new_curator.surname = name[0]
    new_curator.name = name[1]
    new_curator.family = name[2]
    new_curator.position = position

    session.add(new_curator)
    session.commit()

abits = [
    ["abit1@gmail.com", "admin123", ["toropov", "Коля", "vladimirovich"]],
    ["abit2@gmail.com", "admin123", ["toropov", "Коля", "vladimirovich"]],
]


for mail, passw, name in abits:
    new_abit = Abiturient()
    new_abit.email = mail
    new_abit.set_password(passw)

    new_abit.surname = name[0]
    new_abit.name = name[1]
    new_abit.family = name[2]

    # print(form.birthday, form.birthday.data)
    new_abit.birthday = datetime.datetime.strptime("16.12.2003", "%d.%m.%Y")
    new_abit.phone = "+7800000000"
    new_abit.social = "@rjkzavr"
    new_abit.direction = "программирование"
    new_abit.about = "Текст обо мне, как о программисте"
    # new_abit.other_email = form.other_email.data
    new_abit.job = "хакатонщик"
    new_abit.time_job = "долго"

    new_abit.achievements = "Призёр хакатона по разработке промышленного дизайна аэробеспилотника Архипелаг 2023"
    new_abit.motivation_message = "Хочу"

    session.add(new_abit)

    session.add(new_abit)
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

classes = [
    # name, description, academic_email, count_lessons
    ["инжиниринг", "занятие для инженеров", "academic@gmail.com", 4],
    ["программирование", "занятие для программистов", "academic@gmail.com", 3],
    ["моделирование", "занятие для инженеров", "academic@gmail.com", 2],
]

for name, desc, academics_email, count_lessons in classes:
    create_classes(name, academics_email, count_lessons, desc=desc)

classes_add_groups = [
    [1, 1],
    [2, 1],
    [3, 1],
]

for classes_id, group_id in classes_add_groups:
    classes_add_group(classes_id, group_id)

# for name, desc, academics_ids, time, group_ids, auditory in lessons:
#     new_lesson = Lesson()
#     new_lesson.name = name
#     new_lesson.about = desc
#     new_lesson.day_week = time[0]
#     new_lesson.time = time[1]
#     new_lesson.count = time[2]
#     new_lesson.auditory = auditory
#
#     for ind in academics_ids:
#         new_lesson.academics.append(session.query(Academic).get(ind))
#
#     for ind in group_ids:
#         new_lesson.groups.append(session.query(Group).get(ind))
#
#     session.add(new_lesson)
#
#     for group in new_lesson.groups:
#         for stud in group.students:
#             for i in range(time[2]):
#                 new_assessment = Assessment()
#                 new_assessment.student_id = stud.id
#                 new_assessment.lesson_id = new_lesson.id
#                 new_assessment.num = i + 1
#                 session.add(new_assessment)
#
#     session.commit()
#     # print(session.query(Assessment).filter(Assessment.student_id == 1).filter(Assessment.lesson_id == 1).all())

events = [
    # name, description, academics, time [start_time, duration], students
    ["хакатон", "мероприятие для программистов", [3], [datetime.datetime.strptime("27.10.2023", "%d.%m.%Y"), 60], [1]],
]

for name, desc, academics_ids, time, stud_ids in events:
    new_event = Event()
    new_event.name = name
    new_event.about = desc
    new_event.start_time = time[0]
    new_event.duration = time[1]

    for ind in academics_ids:
        new_event.academics.append(session.query(Academic).get(ind))

    for ind in stud_ids:
        new_event.students.append(session.query(Student).get(ind))

    session.add(new_event)
    session.commit()


session.close()
