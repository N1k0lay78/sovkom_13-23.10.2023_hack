from flask import Blueprint
from views.tools import my_render
from data.forms import FormTest

academic_pages = Blueprint('academic', __name__)


@academic_pages.route("/")
def lessons_page():
    return my_render("/academic/index.html", title="Расписание")

@academic_pages.route("/edit_info")
def edit_info_page():
    form = FormTest()
    return my_render("/academic/edit_info.html", title="", form=form)
