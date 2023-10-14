from flask import Flask, render_template, request

from data import db_session
from data.forms import FormDelete
import config

application = Flask(__name__)
application.config.from_object(config)
db_session.global_init("db/study.sqlite")


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


@application.route("/test")
def test_page():
    return my_render("test.html", title="HELLO", name="Данил", knowledges=["JS", "SCSS", "HTML5"])


@application.route("/form", methods=["GET", "POST"])
def form_page():
    name = "Данил"
    form = FormDelete()
    if request.method == 'POST':
        print(f"УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ: {name}")

    return my_render("form.html", title="form", name=name, form=form)


if __name__ == '__main__':
    application.run()
