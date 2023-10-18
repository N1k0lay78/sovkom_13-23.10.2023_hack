from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from data import db_session
import config
from data.users.user import User
from views.index import index_pages
from views.test import test_pages

# create app and apply config
application = Flask(__name__)
application.config.from_object(config)

# init DB
db_session.global_init("db/study.sqlite")

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

if __name__ == '__main__':
    host="0.0.0.0"
    host="192.168.43.33"
    print(f"http://{host}:5000/login")
    print(f"http://{host}:5000/logout")
    print(f"http://{host}:5000/test")
    application.run(host=host, port=5000)
