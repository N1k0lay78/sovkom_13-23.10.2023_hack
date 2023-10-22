import os

from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from data import db_session
import config
from data.users.user import User
from views.abiturient import abiturient_pages
from views.academic import academic_pages
from views.api import api_links
from views.curator import curator_pages
from views.index import index_pages
from views.student import student_pages
from views.test import test_pages

# create app and apply config
application = Flask(__name__)
application.config.from_object(config)

# init DB
db_session.global_init("db/study.sqlite")

# uploads dir
uploads_dir = os.path.join(application.instance_path, 'uploads')
# print(uploads_dir)
try:
    os.makedirs(uploads_dir)
except Exception:
    pass

# login manager
login_manager = LoginManager()
login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user


# SCRF Protection
csrf = CSRFProtect(application)
csrf.init_app(application)

# pages
application.register_blueprint(index_pages)
application.register_blueprint(test_pages, url_prefix='/test')
application.register_blueprint(api_links, url_prefix='/api')
application.register_blueprint(student_pages, url_prefix='/student')
application.register_blueprint(abiturient_pages, url_prefix='/abiturient')
application.register_blueprint(academic_pages, url_prefix='/academic')
application.register_blueprint(curator_pages, url_prefix='/curator')

if __name__ == '__main__':
    host="127.0.0.1"
    # host="192.168.43.33"
    print(f"http://{host}:5000/login")
    print(f"http://{host}:5000/logout")
    print(f"http://{host}:5000/test")
    print(f"http://{host}:5000/api/get_lessons/1")
    application.run(host=host, port=5000)
