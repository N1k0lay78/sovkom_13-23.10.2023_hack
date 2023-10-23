from flask import Blueprint
from views.tools import my_render
from data.forms import FormTest

student_pages = Blueprint('student', __name__)


@student_pages.route("/")
def lessons_page():
    return my_render("/student/index.html", title="Расписание")


@student_pages.route("/edit_info")
def edit_info_page():
    form = FormTest()
    return my_render("/student/edit_info.html", title="", form=form)