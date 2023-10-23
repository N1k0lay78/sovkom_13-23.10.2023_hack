from flask import Blueprint, request, redirect
from flask_login import login_required, current_user

from controller.file import create_file, get_files, get_file_info, delete_file, edit_file
from data.forms import FormFile, FormDelete, FormFileEdit
from views.tools import my_render, goto_profile

curator_pages = Blueprint('curator', __name__)


@curator_pages.route("/")
@login_required
def main_page():
    return my_render("/curator/index.html", title="")


@curator_pages.route("/presentation/create/", methods=["GET", "POST"])
@login_required
def upload_presentation_page():
    form = FormFile()
    error, status = "", "ok"
    if request.method == "POST":
        create_file(form.name.data, request.files["file"], "presentation")
    return my_render("/curator/upload_file.html", title="Загрузка презентации", type="презентацию", error=error,
                     status=status, form=form)


@curator_pages.route("/file/delete/<int:id>", methods=["GET", "POST"])
@login_required
def delete_file_page(id):
    form = FormDelete()

    info = get_file_info(id)
    if info["status"] == "error":
        return goto_profile(current_user)

    error, status, name = "", "ok", info["data"]["name"]
    if request.method == "POST":
        delete_file(id)
        return goto_profile(current_user)

    type = {"presentation": "презентацию", "": ""}[info["data"]["type"]]
    title = {"presentation": "Удаление презентации", "": ""}[info["data"]["type"]]
    return my_render("/curator/delete_file.html", title=title, type=type, error=error,
                     status=status, form=form, asd=name)


@curator_pages.route("/file/<int:id>", methods=["GET", "POST"])
@login_required
def edit_file_page(id):
    form = FormFileEdit()

    info = get_file_info(id)

    error, status, name = "", "ok", info["data"]["name"]

    if not form.name.data:
        form.name.data = info["data"]["name"]
    if not form.href.data:
        form.href.data = info["data"]["href"]

    if request.method == "POST":
        resp = edit_file(id, form.name.data, form.href.data)
        if resp["status"] == "ok":
            return redirect(f"/curator/{info['data']['type']}")
        else:
            error, status = resp["message"], resp["status"]

    type = {"presentation": "презентацию", "": ""}[info["data"]["type"]]
    title = {"presentation": "Редактирование презентации", "": ""}[info["data"]["type"]]
    return my_render("/curator/edit_file.html", title=title, type=type, error=error,
                     status=status, form=form, asd=name)


@curator_pages.route("/presentation/")
@login_required
def presentation_page():
    files = get_files("presentation")["data"]
    return my_render("/curator/file.html", title="Презентации", type="презентаций", files=files, t="presentation")
