import os

from flask import Blueprint, request, redirect, send_file
from flask_login import login_user, login_required, logout_user, current_user

from config import uploads_dir
from controller.file import get_file_path
from data import db_session
from data.forms import FormLogin
from data.users.user import User
from views.tools import my_render, goto_profile

index_pages = Blueprint('index', __name__)


@index_pages.route("/login/", methods=["GET", "POST"])
def login_page():
    form = FormLogin()
    error = ""
    if request.method == "POST":
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        print(user)
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return goto_profile(user)
        else:
            error = "Неверная почта или пароль"
    print(error)
    return my_render("login.html", title="Логин", form=form, error=error)


@index_pages.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect("/")


@index_pages.route("/file/<string:href>")
@login_required
def load_file(href):
    resp = get_file_path(href)
    if resp["status"] == "error":
        return goto_profile(current_user)
    return send_file(os.path.join(uploads_dir, resp["filename"]))


@index_pages.route("/")
def main_page():
    return goto_profile(current_user)