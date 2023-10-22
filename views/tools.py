from flask import render_template, redirect
from flask_login import current_user

from data import db_session
from data.users.academic import Academic
from data.users.curator import Curator
from data.users.student import Student


def my_render(filename, **kwargs):
    my_kwargs = {
        "need_log": True,
        "is_authorized": current_user.is_authenticated,
        "is_logout": False,
        "user_id": current_user.id if current_user.is_authenticated else -1,
        "type": current_user.type if current_user.is_authenticated else "unauthorized",
        "user": current_user,
    }
    if current_user.is_authenticated:
        session = db_session.create_session()
        if current_user.type == "student":
            my_kwargs["student"] = session.query(Student).get(current_user.id)
        elif current_user.type == "academic":
            my_kwargs["academic"] = session.query(Academic).get(current_user.id)
        elif current_user.type == "curator":
            my_kwargs["curator"] = session.query(Curator).get(current_user.id)
    for key, val in kwargs.items():
        my_kwargs[key] = val
    return render_template(filename, **my_kwargs)


def goto_profile(user):
    if not user.is_authenticated:
        return redirect("/login")
    if user.type == "abiturient":
        return redirect("/abiturient/")
    elif user.type == "student":
        return redirect("/student/")
    elif user.type == "academic":
        return redirect("/academic/")
    elif user.type == "curator":
        return redirect("/curator/")
