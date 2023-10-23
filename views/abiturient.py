from flask import Blueprint, request, redirect

from controller.abiturient import create_abiturient
from data.forms import FormTest, FormSendMessage, FormAbit
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


@abiturient_pages.route("/edit_info")
def edit_info_page():
    form = FormTest()
    return my_render("/abiturient/edit_info.html", title="", form=form)

@abiturient_pages.route("/edit_password")
def edit_password_page():
    form = FormTest()
    return my_render("/abiturient/edit_password.html", title="", form=form)
