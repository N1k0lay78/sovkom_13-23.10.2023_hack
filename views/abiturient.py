from flask import Blueprint

from data.forms import FormTest
from views.tools import my_render

abiturient_pages = Blueprint('abiturient', __name__)



@abiturient_pages.route("/")
def main_page():
    return my_render("/abiturient/index.html", title="")


@abiturient_pages.route("/application")
def application_page():
    form = FormTest()
    return my_render("/abiturient/application.html", title="", form=form)


@abiturient_pages.route("/edit_info")
def edit_info_page():
    form = FormTest()
    return my_render("/abiturient/edit_info.html", title="", form=form)
