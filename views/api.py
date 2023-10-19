from flask import Blueprint, request
import jsonpickle

jsonpickle.set_preferred_backend('json')
jsonpickle.set_encoder_options('json', ensure_ascii=False)

from controller.user import get_lessons, get_assessments

api_links = Blueprint('api', __name__)


@api_links.route("/get_lessons/<int:group_id>/")
def get_lesson(group_id):
    ans = get_lessons(group_id)
    return jsonpickle.encode(ans)


@api_links.route("/get_assessments/<int:group_id>/<int:lesson_id>")
def get_assessment(group_id, lesson_id):
    ans = get_assessments(group_id, lesson_id)
    # print(ans)
    return jsonpickle.encode(ans)