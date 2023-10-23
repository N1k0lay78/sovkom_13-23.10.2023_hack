from flask import Blueprint, request, redirect
from flask_login import login_required, current_user

from controller.abiturient import get_abits
from controller.file import create_file, get_files, get_file_info, delete_file, edit_file
from controller.lessons import create_classes, get_all_classes, classes_add_group
from data.forms import FormFile, FormDelete, FormFileEdit, FormCreateClasses, FormClassesSetGroup
from data.forms import FormFile, FormDelete, FormFileEdit, FormCreateAcademic, FormEditInfo, FormCreateGroup, \
    FormEditPassword, FormTreatment, FormEditLessonForCurator
from views.tools import my_render, goto_profile
from flask import Blueprint
from views.tools import my_render
from data.forms import FormTest

curator_pages = Blueprint('curator', __name__)


@curator_pages.route("/")
@login_required
def main_page():
    return my_render("/curator/index.html", title="")


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

    type = {"presentation": "презентацию", "abstract": "конспект", "video": "видео", "file": "файла", "": ""}[
        info["data"]["type"]]
    title = {"presentation": "Удаление презентации", "abstract": "Удаление конспекта", "video": "Удалить видео",
             "file": "Удалить файл", "": ""}[info["data"]["type"]]
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

    type = {"presentation": "презентацию", "abstract": "конспект", "video": "видео", "file": "файл", "": ""}[
        info["data"]["type"]]
    title = {"presentation": "Редактирование презентации", "abstract": "Редактирование конспекта",
             "video": "Редактирование видео", "file": "Редактирование файла", "": ""}[info["data"]["type"]]
    return my_render("/curator/edit_file.html", title=title, type=type, error=error,
                     status=status, form=form, asd=name)


@curator_pages.route("/presentation/")
@login_required
def presentation_page():
    files = get_files("presentation")["data"]
    return my_render("/curator/file.html", title="Презентации", type="презентаций", files=files, t="presentation")


@curator_pages.route("/presentation/create/", methods=["GET", "POST"])
@login_required
def upload_presentation_page():
    form = FormFile()
    error, status = "", "ok"
    if request.method == "POST":
        resp = create_file(form.name.data, request.files["file"], "presentation")
        if resp["status"] != "ok":
            error, status = resp["message"], resp["status"]
        else:
            return redirect("/curator/presentation")
    return my_render("/curator/upload_file.html", title="Загрузка презентации", type="презентацию", error=error,
                     status=status, form=form)


@curator_pages.route("/abstract/")
@login_required
def abstract_page():
    files = get_files("abstract")["data"]
    return my_render("/curator/file.html", title="Конспекты", type="конспектов", files=files, t="abstract")


@curator_pages.route("/abstract/create/", methods=["GET", "POST"])
@login_required
def upload_abstract_page():
    form = FormFile()
    error, status = "", "ok"
    if request.method == "POST":
        resp = create_file(form.name.data, request.files["file"], "abstract")
        if resp["status"] != "ok":
            error, status = resp["message"], resp["status"]
        else:
            return redirect("/curator/abstract")
    return my_render("/curator/upload_file.html", title="Загрузка конспекта", type="конспект", error=error,
                     status=status, form=form)


@curator_pages.route("/video/")
@login_required
def video_page():
    files = get_files("video")["data"]
    return my_render("/curator/file.html", title="Видео", type="видео", files=files, t="video")


@curator_pages.route("/video/create/", methods=["GET", "POST"])
@login_required
def upload_video_page():
    form = FormFile()
    error, status = "", "ok"
    if request.method == "POST":
        resp = create_file(form.name.data, request.files["file"], "video")
        if resp["status"] != "ok":
            error, status = resp["message"], resp["status"]
        else:
            return redirect("/curator/video")
    return my_render("/curator/upload_file.html", title="Загрузка видео", type="видео", error=error,
                     status=status, form=form)


@curator_pages.route("/file/")
@login_required
def file_page():
    files = get_files("file")["data"]
    return my_render("/curator/file.html", title="Файлы", type="", files=files, t="file")


@curator_pages.route("/file/create/", methods=["GET", "POST"])
@login_required
def upload_file_page():
    form = FormFile()
    error, status = "", "ok"
    if request.method == "POST":
        resp = create_file(form.name.data, request.files["file"], "file")
        if resp["status"] != "ok":
            error, status = resp["message"], resp["status"]
        else:
            return redirect("/curator/file")
    return my_render("/curator/upload_file.html", title="Загрузка файла", type="файл", error=error,
                     status=status, form=form)


@curator_pages.route("/create_academic", methods=["GET", "POST"])
def create_academic_page():
    form = FormCreateAcademic()
    error, status = "", ""
    if request.method == "POST":
        # resp = create_academic(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/curator/create_academic.html", title="", form=form)


@curator_pages.route("/create_group", methods=["GET", "POST"])
def create_group_page():
    form = FormCreateGroup()
    error, status = "", ""
    if request.method == "POST":
        # resp = create_group(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/curator/create_group.html", title="", form=form)


@curator_pages.route("/edit_info", methods=["GET", "POST"])
def edit_info_page():
    form = FormEditInfo()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_abiturient(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/curator/edit_info.html", title="", form=form)


@curator_pages.route("/create_classes", methods=["GET", "POST"])
def create_classes_page():
    form = FormCreateClasses()
    error, status = "", "ok"
    if request.method == "POST":
        resp = create_classes(form.name.data, form.academic.data, form.count.data)
        if resp["status"] != "ok":
            error, status = resp["message"], resp["status"]
        else:
            return redirect("/curator/classes")
    return my_render("/curator/create_classes.html", title="Создание урока", error=error,
                     status=status, form=form)


@curator_pages.route("/classes_group/<int:id>", methods=["GET", "POST"])
def classes_add_group_page(id):
    form = FormClassesSetGroup()
    error, status = "", "ok"
    if request.method == "POST":
        resp = classes_add_group(id, form.group.data)
        if resp["status"] != "ok":
            error, status = resp["message"], resp["status"]
        else:
            return redirect("/curator/classes")
    return my_render("/curator/classes_add_group.html", title="Задать группу", error=error,
                     status=status, form=form)


@curator_pages.route("/classes")
def classes_page():
    resp = get_all_classes()
    return my_render("/curator/classes.html", title="Список уроков", data=resp["data"])


@curator_pages.route("/abit")
def abit_page():
    resp = get_abits()
    return my_render("/curator/abit_list.html", title="Список абитуриентов", data=resp["data"])


@curator_pages.route("/abit/accept/<int:id>", methods=["GET", "POST"])
def abit_accept_page():
    # resp = get_abits()
    # форма
    return my_render("/curator/abit_list.html", title="Принять абитуриента")


@curator_pages.route("/edit_password", methods=["GET", "POST"])
def edit_password_page():
    form = FormEditPassword()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_password(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/curator/edit_password.html", title="", form=form)


@curator_pages.route("/treatment", methods=["GET", "POST"])
def treatment_page():
    form = FormTreatment()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_password(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/curator/tratment.html", title="", form=form)


@curator_pages.route("/edit_lesson_for_curator", methods=["GET", "POST"])
def edit_lesson_page():
    form = FormEditLessonForCurator()
    error, status = "", ""
    if request.method == "POST":
        # resp = edit_password(form)
        # if resp["status"] == "error":
        #     error, status = resp["message"], resp["status"]
        pass
    return my_render("/curator/edit_lesson.html", title="", form=form)
