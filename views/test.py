from flask import Blueprint, request
from views.tools import my_render
import requests
import json
from data.forms import FormDelete

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
    # res = json.loads(requests.get("http://127.0.0.1:5000/api/get_assessments/1/1").json()['data'])
    # print(type(res))
    res = {"header": ["Студент", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Итого"], "tabel": [{"name": "Студент Коля", "data": [[4, 1], [5, 1], [-1, 0], [3, 1], [-1, 0], [-1, 0], [-1, 1], [-1, 0], [-1, 0], [-1, 0]], "result": '-'}, {"name": "Студент Аня", "data": [[-1, 1], [-1, 1], [-1, 0], [-1, 0], [-1, 0], [3, 1], [-1, 0], [-1, 0], [-1, 0], [-1, 0]], "result": '-'},
                                                                                                        {"name": "Студент Кто", "data": [[-1, 0], [5, 1], [-1, 0], [5, 1], [-1, 0], [-1, 1], [-1, 1], [-1, 1], [-1, 0], [-1, 0]], "result": '-'}, {"name": "Студент Что", "data": [[-1, 1], [4, 1], [-1, 0], [-1, 0], [-1, 1], [3, 1], [-1, 0], [-1, 1], [-1, 0], [-1, 0]], "result": '-'},
                                                                                                        {"name": "Студент Когда", "data": [[4, 1], [2, 1], [-1, 0], [3, 1], [-1, 0], [-1, 0], [-1, 1], [-1, 0], [-1, 0], [-1, 0]], "result": '-'}, {"name": "Студент Где", "data": [[5, 1], [-1, 1], [5, 1], [-1, 0], [-1, 0], [-1, 1], [-1, 0], [-1, 0], [5, 1], [-1, 0]], "result": '-'}]}

    return my_render("/test/tabel.html", title="Таблица успеваемости", header_table=res['header'][1:-1], table_len=len(res['header']), stud_data=res['tabel'])




@test_pages.route("/form/", methods=["GET", "POST"])
def form_page():
    name = "Данил"
    form = FormDelete()
    if request.method == 'POST':
        print(f"УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ: {name}")

    return my_render("/test/form.html", title="form", name=name, form=form)
