from flask import Blueprint
from flask_login import login_required, current_user

from controller.student import get_lesson_of_user
from views.tools import my_render

student_pages = Blueprint('student', __name__)


@student_pages.route("/")
@login_required
def lessons_page():
    lessons = get_lesson_of_user(current_user.id)
    print(lessons)
    message = lessons["message"]
    lessons = lessons["data"]
    day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
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
