from flask import Blueprint, request
from flask import Flask
from views.tools import my_render
import requests
import json
from data.forms import FormDelete, FormLogin, FormTest

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


@test_pages.route("/tabel/", methods=["GET", "POST"])
def test_tabel_page():
    # res = json.loads(requests.get("http://127.0.0.1:5000/api/get_assessments/1/1").json()['data'])
    # print(type(res))
    user = 'Преподаватель'
    res = {"header": ["Студент", "11.12", "12.12", "3.01", "4.01", "5.01", "6.01", "7.01", "8.01", "19.01", "20.01", "Итого"], "tabel": [{"name": "Студент Коля", "data": [[4, 1], [5, 1], [-1, 0], [3, 1], [-1, 0], [-1, 0], [-1, 1], [-1, 0], [-1, 0], [-1, -1]], "result": '-'}, {"name": "Студент Аня", "data": [[-1, 1], [-1, 1], [-1, 0], [-1, 0], [-1, 0], [3, 1], [-1, 0], [-1, 0], [-1, 0], [-1, -1]], "result": '-'},
                                                                                                        {"name": "Студент Кто", "data": [[-1, 0], [5, 1], [-1, 0], [5, 1], [-1, 0], [-1, 1], [-1, 1], [-1, 1], [-1, 0], [-1, -1]], "result": '-'}, {"name": "Студент Что", "data": [[-1, 1], [4, 1], [-1, 0], [-1, 0], [-1, 1], [3, 1], [-1, 0], [-1, 1], [-1, 0], [-1, -1]], "result": '-'},
                                                                                                        {"name": "Студент Когда", "data": [[4, 1], [2, 1], [-1, 0], [3, 1], [-1, 0], [-1, 0], [-1, 1], [-1, 0], [-1, 0], [-1, -1]], "result": '-'}, {"name": "Студент Где", "data": [[5, 1], [-1, 1], [5, 1], [-1, 0], [-1, 0], [-1, 1], [-1, 0], [-1, 0], [5, 1], [-1, -1]], "result": '-'}]}
    if request.method == "POST":
        date_form = list((dict(request.form)).values())[1:]
        print(date_form)
        rez = dict()
        rez["header"] = res['header']
        l_rez =[]
        iter = 0
        for i in res['tabel']:
            d = {}
            d['name'] = i['name']
            list_date = []
            print(len(res['header'][1:-1]))
            for j in range(len(res['header'][1:-1])):
                if date_form[j+iter] != '':
                    list_date.append([date_form[j+iter], 1])
                else:
                    list_date.append(i['data'][j])
            d['data'] = list_date
            iter += len(res['header'][1:-1])
            l_rez.append(d)
        rez['tabel'] = l_rez
        res = rez

    form = FormLogin()
    print(res)

    return my_render("/test/tabel.html", title="Таблица успеваемости", header_table=res['header'][1:-1],
                     table_len=len(res['header']), stud_data=res['tabel'], user=user, form=form)


@test_pages.route("/forms/", methods=["GET", "POST"])
def test_form_render():
    form = FormTest()
    return my_render("/test/ui_kit_form.html", form=form, error="Всё не так, давай по новой")


@test_pages.route("/timetable/")
def test_timetable_page():
    table = [
        ["Понедельник", [["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                         ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                         ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                         ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"]]],
        ["Вторник", [["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                     ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                     ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                     ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"]]],
        ["Среда", [["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                   ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                   ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"],
                   ["14:00-15:30", 1, "Программирование", "Профессор Николай", "У 115"]]],
    ]
    return my_render("/test/timetable.html", title="Расписание", table=table)


@test_pages.route("/form/", methods=["GET", "POST"])
def form_page():
    name = "Данил"
    form = FormDelete()
    if request.method == 'POST':
        print(f"УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ: {name}")

    return my_render("/test/form.html", title="form", name=name, form=form)
