from flask import Blueprint
from views.tools import my_render

academic_pages = Blueprint('academic', __name__)


@academic_pages.route("/")
def lessons_page():
    return my_render("/academic/index.html", title="Расписание")

