from flask import Blueprint
from views.tools import my_render

curator_pages = Blueprint('curator', __name__)


@curator_pages.route("/")
def main_page():
    return my_render("/curator/index.html", title="")


@curator_pages.route("/presentation")
def main_page():
    return my_render("/curator/upload_file.html", title="Загрузка презентации", type="презентацию")