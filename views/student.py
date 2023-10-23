from flask import Blueprint, request
from flask_login import login_required, current_user

from controller.message import send, recv_messages
from controller.student import get_lesson_of_user
from data.forms import FormSendMessage, FormEditPassword, FormEditInfo
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
    return "Задачи"


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
    return "Предметы и успеваемость"


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
