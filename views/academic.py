from flask import Blueprint, request
from views.tools import my_render
from data.forms import FormTest, FormEditPassword, FormEditInfo, FormExamination, FormEditLesson

academic_pages = Blueprint('academic', __name__)


@academic_pages.route("/")
def lessons_page():
    return my_render("/academic/index.html", title="Расписание")

@academic_pages.route("/edit_info", methods=["GET", "POST"])
def edit_info_page():
    form = FormEditInfo()
    error, status = "", ""
    if request.method == "POST":
        #resp = edit_abiturient(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/academic/edit_info.html", title="", form=form)


@academic_pages.route("/edit_password", methods=["GET", "POST"])
def edit_password_page():
    form = FormEditPassword()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_password(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/academic/edit_password.html", title="", form=form)

@academic_pages.route("/examination", methods=["GET", "POST"])
def examination_page():
    form = FormExamination()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_password(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/academic/treatment", title="", form=form)


@academic_pages.route("/edit_lesson", methods=["GET", "POST"])
def edit_lesson_page():
    form = FormEditLesson()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_password(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/academic/edit_lesson.html", title="", form=form)
