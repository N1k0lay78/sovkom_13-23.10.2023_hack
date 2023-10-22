from flask import Blueprint
from views.tools import my_render

abiturient_pages = Blueprint('abiturient', __name__)


@abiturient_pages.route("/")
def main_page():
    return my_render("/abiturient/index.html", title="")