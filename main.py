from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, logout_user, login_required, login_user, current_user
from data import db_session
from data.forms import FormDelete, FormLogin
import config
from data.users.user import User

application = Flask(__name__)
application.config.from_object(config)
db_session.global_init("db/study.sqlite")
login_manager = LoginManager()
login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user


def my_render(filename, **kwargs):
    my_kwargs = {
        "need_log": True,
        "is_authorized": False,
        "is_logout": False,
        "user_id": -1,
    }
    for key, val in kwargs.items():
        my_kwargs[key] = val
    return render_template(filename, **my_kwargs)


@application.route("/login/", methods=["GET", "POST"])
def login_page():
    form = FormLogin()
    error = ""
    if request.method == "POST":
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        print(user, 123)
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            print(user)
            return redirect("/")
        else:
            error = "Неверный логин или пароль"
    return my_render("login.html", title="Логин", form=form, error=error)


@application.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect("/")


@application.route("/test")
def test_page():
    return my_render("base.html", title="HELLO", name="Данил", knowledges=["JS", "SCSS", "HTML5"])

@application.route("/base")
def base():
    return my_render("base.html", title="HELLO", name="Данил", knowledges=["JS", "SCSS", "HTML5"])
@application.route("/form", methods=["GET", "POST"])
def form_page():
    name = "Данил"
    form = FormDelete()
    if request.method == 'POST':
        print(f"УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ: {name}")

    return my_render("form.html", title="form", name=name, form=form)


if __name__ == '__main__':
    application.run()
