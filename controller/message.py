from data import db_session
from data.message.message import Message
from data.users.user import User


def send(send_user_id, recv_user_email, message):
    session = db_session.create_session()
    send = session.query(User).get(send_user_id)
    recv = session.query(User).filter(User.email == recv_user_email).first()
    if not send:
        session.close()
        return {"status": "error", "message": "отправитель не существует"}
    if not recv:
        session.close()
        return {"status": "error", "message": "получатель не найден"}
    if send.id == recv.id:
        session.close()
        return {"status": "error", "message": "нельзя отправлять сообщения себе"}
    if not message:
        session.close()
        return {"status": "error", "message": "пустое сообщение"}

    new_message = Message()
    new_message.send_user_id = send.id
    new_message.recv_user_id = recv.id
    new_message.message = message

    session.add(new_message)
    session.commit()

    session.close()
    return {"status": "ok", "message": "сообщение отправлено"}


def recv_messages(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)

    if not user:
        session.close()
        return {"status": "error", "message": "получатель не существует"}

    messages = session.query(Message).filter(Message.recv_user_id == user.id).all()

    if not messages:
        session.close()
        return {"status": "ok", "message": "нету сообщения", "data": []}

    msgs = []
    for message in messages:
        sender = session.query(User).get(message.send_user_id)
        if not sender:
            name = ""
        else:
            name = sender.name
        msgs.append({"send_name": name, "message": message.message, "read": message.read, "time": message.time_created,
                     "id": message.id})

    session.close()
    return {"status": "ok", "message": "", "data": msgs}


def sended(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)

    if not user:
        session.close()
        return {"status": "error", "message": "отправитель не существует"}

    messages = session.query(Message).filter(Message.send_user_id == user.id).all()

    if not messages:
        session.close()
        return {"status": "ok", "message": "нету сообщения", "data": []}

    msgs = []
    for message in messages:
        sender = session.query(User).get(message.recv_user_id)
        if not sender:
            name = ""
        else:
            name = sender.name
        msgs.append({"recv_name": name, "message": message.message, "read": message.read, "time": message.time_created,
                     "id": message.id})

    session.close()
    return {"status": "ok", "message": "", "data": msgs}


def read_message(user_id, message_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)

    if not user:
        session.close()
        return {"status": "error", "message": "получатель не существует"}

    message = session.query(Message).get(message_id)

    if not message:
        session.close()
        return {"status": "error", "message": "нету сообщения"}

    if message.recv_user_id == user.id:
        session.close()
        return {"status": "error", "message": "нету сообщения"}

    message.read = True
    session.add(message)
    session.commit()

    session.close()
    return {"status": "ok", "message": "сообщение прочитано"}


