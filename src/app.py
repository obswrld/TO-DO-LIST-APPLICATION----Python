from flask import Flask
from dotenv import load_dotenv
load_dotenv()

from config.config import DevelopmentConfig
from src.schemas.extensions import db
from src.controllers.user_controller import user_controller
from src.controllers.task_controller import task_controller
from src.controllers.label_controller import label_controller
from src.config.config import DevelopmentConfig

def create_app():
    app = Flask(__name__)


    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    app.register_blueprint(label_controller, url_prefix='/label')
    app.register_blueprint(task_controller, url_prefix='/api/task')
    app.register_blueprint(user_controller, url_prefix='/api/user')

    @app.before_request
    def create_tables():
        db.create_all()

    @app.route('/')
    def index():
        return "Welcome to ToDo List API!"
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)