from flask import Blueprint, request
from views.tools import my_render

from data.forms import FormDelete, FormTest

test_pages = Blueprint('test', __name__)


@test_pages.route("/")
def test_page():
    return my_render("/test/index.html", title="HELLO")


@test_pages.route("/profile/")
def test_profile_page():
    return my_render("/test/profile.html", title="HELLO")


@test_pages.route("/base/")
def test_base_page():
    return my_render("/test/base.html", title="HELLO")


@test_pages.route("/tabel/")
def test_tabel_page():
    return my_render("/test/tabel.html", title="Таблица успеваемости")


@test_pages.route("/forms/", methods=["GET", "POST"])
def test_form_render():
    form = FormTest()
    return my_render("/test/ui_kit_form.html", form=form, error="Всё не так, давай по новой")


@test_pages.route("/form/", methods=["GET", "POST"])
def form_page():
    name = "Данил"
    form = FormDelete()
    if request.method == 'POST':
        print(f"УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ: {name}")

    return my_render("/test/form.html", title="form", name=name, form=form)
