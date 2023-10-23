from data import db_session
from data.users.abiturient import Abiturient
from data.users.user import User


def create_abiturient(form):
    session = db_session.create_session()

    if session.query(User).filter(User.email == form.email.data).first():
        session.close()
        return {"status": "error", "message": "пользователь с такой почтой уже существует"}

    if form.password.data != form.repeat_password.data:
        print(form.password.data, form.repeat_password.data)
        session.close()
        return {"status": "error", "message": "пароли не совпадают"}

    new_abit = Abiturient()
    new_abit.email = form.email.data
    new_abit.set_password(form.password.data)

    new_abit.name = form.name.data
    new_abit.surname = form.surname.data
    new_abit.family = form.family.data

    # print(form.birthday, form.birthday.data)
    new_abit.birthday = form.birthday.data
    new_abit.phone = form.phone.data
    new_abit.social = form.social.data
    new_abit.direction = ["Программирование", "Математика", "Экономика", "Физика"][int(form.direction.data) - 1]
    new_abit.about = form.about.data
    # new_abit.other_email = form.other_email.data
    new_abit.job = form.job.data
    new_abit.time_job = form.time_job.data

    new_abit.achievements = form.achievements.data
    new_abit.motivation_message = form.motivation_message.data

    session.add(new_abit)
    session.commit()
    session.close()

    return {"status": "ok", "message": "абитуриент создан"}


def get_abits():
    session = db_session.create_session()

    abits = session.query(Abiturient).all()

    if not abits:
        session.close()
        return {"status": "ok", "message": "абитуриентов нет", "data": []}

    data = []
    for abit in abits:
        data.append({
            "id": abit.id,
            "email": abit.email,
            "fullname": f"{abit.surname} {abit.name} {abit.family}",
            "contacts": [abit.phone, abit.social],
            "birthday": abit.birthday,
            "job": [abit.job, abit.time_job],
            "direction": abit.direction,
            # "other_email": abit.other_email,
            "about": abit.about,
            "achievements": abit.achievements,
            "motivation_message": abit.motivation_message,
            "accept": abit.accept,
        })

    session.close()
    return {"status": "ok", "message": "", "data": data}


def accept_abit(id):
    session = db_session.create_session()

    abit = session.query(Abiturient).get(id)

    if not abit:
        session.close()
        return {"status": "error", "message": "абитуриент не найден"}

    abit.accept = True

    session.add(abit)
    session.commit()
    session.close()

    return {"status": "ok", "message": "абитуриент принят"}
