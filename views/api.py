from flask import Blueprint, request
from jsonpickle import json

from controller.user import get_lessons

api_links = Blueprint('api', __name__)


@api_links.route("/get_lessons/<int:group_id>/")
def get_lesson(group_id):
    print(get_lessons(group_id))
    answer = {}
    return json.encode(answer)