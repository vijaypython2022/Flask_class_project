from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db=SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__,template_folder="templates")

    app.config.from_object(app_config[config_name])

    from p1.user.views import app as users_module
    from p1.Employee_info.views import mod as emp_module
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    app.register_blueprint(users_module)
    app.register_blueprint(emp_module)

    return app
