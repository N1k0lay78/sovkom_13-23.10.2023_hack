from data import db_session
from data.users.academic import Academic
from data.users.curator import Curator
from data.users.student import Student
from data.users.user import User

db_session.global_init("db/study.sqlite")

session = db_session.create_session()

students = [
    ["student@gmail.com", "admin123", "Студент Коля"],
]

for mail, passw, name in students:
    new_student = Student()
    new_student.email = mail
    new_student.set_password(passw)
    new_student.name = name

    session.add(new_student)
    session.commit()

academic = [
    ["academic@gmail.com", "admin123", "Академик Николай", "Профессор"],
]

for mail, passw, name, position in academic:
    new_academic = Academic()
    new_academic.email = mail
    new_academic.set_password(passw)
    new_academic.name = name
    new_academic.position = position

    session.add(new_academic)
    session.commit()

session.close()

curator = [
    ["curator@gmail.com", "admin123", "Куратор Николай Владимирович", "Курирует всё"],
]

for mail, passw, name, position in curator:
    new_curator = Curator()
    new_curator.email = mail
    new_curator.set_password(passw)
    new_curator.name = name
    new_curator.position = position

    session.add(new_curator)
    session.commit()

session.close()
