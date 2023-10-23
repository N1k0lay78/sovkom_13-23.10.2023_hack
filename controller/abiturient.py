from data import db_session
from data.users.abiturient import Abiturient
from data.users.user import User


def create_abiturient(form):
    session = db_session.create_session()

    if session.query(User).filter(User.email == form.email.data).first():
        session.close()
        return {"status": "error", "message": "пользователь с такой почтой уже существует"}

    if form.password.data == form.repeat_password.data:
        session.close()
        return {"status": "error", "message": "пароли не совпадают"}


    new_abit = Abiturient()
    new_abit.email = form.email.data
    new_abit.set_password(form.password.data)

    session.add(new_abit)
    session.commit()
    session.close()

    return {"status": "ok", "message": "абитуриент создан"}