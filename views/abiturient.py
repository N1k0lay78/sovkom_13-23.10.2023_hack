from flask import Blueprint, request, redirect

from controller.abiturient import create_abiturient
from data.forms import FormTest, FormSendMessage, FormAbit, FormEditInfo, FormEditPassword
from views.tools import my_render

abiturient_pages = Blueprint('abiturient', __name__)


@abiturient_pages.route("/")
def main_page():
    return my_render("/abiturient/index.html", title="")


@abiturient_pages.route("/application", methods=["GET", "POST"])
def application_page():
    form = FormAbit()
    error, status = "", ""
    if request.method == "POST":
        resp = create_abiturient(form)
        if resp["status"] == "error":
            error, status = resp["message"], resp["status"]
            print(error)
        else:
            return redirect("/")
    return my_render("/abiturient/application.html", title="", form=form, error=error, status=status)


@abiturient_pages.route("/edit_info", methods=["GET", "POST"])
def edit_info_page():
    form = FormEditInfo()
    error, status = "", ""
    if request.method == "POST":
        resp = edit_abiturient(form)
        if resp["status"] == "error":
            error, status = resp["message"], resp["status"]
    return my_render("/abiturient/edit_info.html", title="", form=form)

@abiturient_pages.route("/edit_password", methods=["GET", "POST"])
def edit_password_page():
    form = FormEditPassword()
    error, status = "", ""
    if request.method == "POST":
        resp = edit_password(form)
        if resp["status"] == "error":
            error, status = resp["message"], resp["status"]
    return my_render("/abiturient/edit_password.html", title="", form=form)
