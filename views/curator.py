from flask import Blueprint
from views.tools import my_render
from data.forms import FormTest

curator_pages = Blueprint('curator', __name__)


@curator_pages.route("/")
def main_page():
    return my_render("/curator/index.html", title="")


@curator_pages.route("/create_academic")
def create_academic_page():
    form = FormTest()
    return my_render("/curator/create_academic.html", title="", form=form)


@curator_pages.route("/create_group")
def create_group_page():
    form = FormTest()
    return my_render("/curator/create_group.html", title="", form=form)

