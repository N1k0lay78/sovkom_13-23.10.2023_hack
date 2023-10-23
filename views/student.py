from flask import Blueprint, request
from flask_login import login_required, current_user

from controller.lessons import get_all_classes, get_stud_classes
from controller.message import send, recv_messages
from controller.student import get_lesson_of_user
from data.forms import FormSendMessage, FormEditPassword, FormEditInfo, FormLogin
from views.tools import my_render, goto_profile
from flask import Blueprint
from views.tools import my_render
from data.forms import FormTest

student_pages = Blueprint('student', __name__)


@student_pages.route("/")
@login_required
def lessons_page():
    lessons = get_lesson_of_user(current_user.id)
    message = lessons["message"]
    lessons = lessons["data"]
    day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(lessons)
    return my_render("/student/lessons.html", title="Расписание", message=message, table=lessons, day=day)


@student_pages.route("/tasks")
@login_required
def tasks_page():
    resp = get_all_classes()
    return my_render("/student/works.html", title="Задачи", data=resp["data"])


@student_pages.route("/info")
@login_required
def info_page():
    return "Информация о студенте"


@student_pages.route("/info/<int:id>")
@login_required
def info_id_page():
    return "Информация о другом студенте"


@student_pages.route("/assessments/")
@login_required
def assessments_page():
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

    return my_render("/student/assessment.html", title="Таблица успеваемости", header_table=res['header'][1:-1],
                     table_len=len(res['header']), stud_data=res['tabel'], user=user, form=form)


@student_pages.route("/assessment/<int:id>")
@login_required
def assessment_page():
    return "Успеваемость по предмету"


@student_pages.route("/send", methods=["GET", "POST"])
@login_required
def send_page():
    form = FormSendMessage()
    error, status = "", "ok"
    if request.method == "POST":
        resp = send(current_user.id, form.email.data, form.message.data)
        error, status = resp["message"], resp["status"]
        if status == "ok":
            return goto_profile(current_user)
    return my_render("/student/send.html", form=form, error=error, status=status)


@student_pages.route("/read")
@login_required
def read_page():
    recv = recv_messages(current_user.id)
    if recv["status"] == "ok":
        data = recv["data"]
    else:
        data = []
    print(data)
    return my_render("/student/read.html", error=recv["message"], status=recv["status"], data=data)


@student_pages.route("/edit_info", methods=["GET", "POST"])
def edit_info_page():
    form = FormEditInfo()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_abiturient(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/student/edit_info.html", title="", form=form)


@student_pages.route("/edit_password", methods=["GET", "POST"])
def edit_password_page():
    form = FormEditPassword()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_password(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/student/edit_password.html", title="", form=form)
