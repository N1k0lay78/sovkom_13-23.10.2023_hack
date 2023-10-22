from flask import Blueprint
from views.tools import my_render

student_pages = Blueprint('student', __name__)


@student_pages.route("/")
def lessons_page():
    return my_render("/student/index.html", title="Расписание")