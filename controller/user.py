import jsonpickle
from data import db_session
from data.education.assessments import Assessment
from data.users.group import Group

jsonpickle.set_preferred_backend('json')
jsonpickle.set_encoder_options('json', ensure_ascii=False)


def get_lessons(group_id):
    session = db_session.create_session()
    group = session.query(Group).get(group_id)
    if not group:
        session.close()
        return {"status": "error", "message": "группа не существует"}

    classes = group.classes
    if not classes:
        session.close()
        return {"status": "ok", "message": "занятий нет", "data": {}}

    data = [[] for _ in range(7)]

    for classe in classes:
        for lesson in classe.lessons:
            if lesson.public:
                data[int(lesson.day_week - 1)].append({
                    "time": ":".join(str(lesson.date.time()).split(":")[:-1]),
                    "type_week": lesson.type_week,
                    "name": lesson.classes.name,
                    "description": lesson.classes.description,
                    "academic_name": lesson.classes.academics[0].name,
                    "auditory": lesson.auditory,
                })
    session.close()

    for i in range(7):
        data[i].sort(key=lambda x: x["time"])

    return {"status": "ok", "message": "", "data": data}


def get_assessments(group_id, lesson_id):
    session = db_session.create_session()
    group = session.query(Group).get(group_id)
    if not group:
        session.close()
        return {"status": "error", "message": "группа не существует"}
    student_ids = [student.id for student in group.students]
    if not student_ids:
        session.close()
        return {"status": "error", "message": "в группе нет студентов"}
    lesson = session.query(Lesson).get(lesson_id)
    print(lesson)
    if not lesson:
        session.close()
        return {"status": "error", "message": "урок не существует"}
    tabel = {"header": ["Студент"] + [str(i + 1) for i in range(lesson.count)] + ["Итого"],
             "tabel": []}
    for student in group.students:
        data = []
        stud_assessments = session.query(Assessment).filter(
            Assessment.lesson_id == lesson_id,
            Assessment.student_id == student.id
        ).order_by(Assessment.num).all()
        summ = 0
        for assessment in stud_assessments:
            data.append([assessment.mark if assessment.mark else -1, int(assessment.visit)])
            summ += assessment.mark if assessment.mark else 0

        max_mark = 5

        line = {"name": student.name, "data": data, "result": round(summ / max_mark / lesson.count * 100)}
        tabel["tabel"].append(line)
    session.close()
    # print(tabel)
    return {"status": "ok", "message": "", "data": jsonpickle.encode(tabel)}
