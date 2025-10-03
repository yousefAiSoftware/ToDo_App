from flask import Flask
from config import Config
from models.database import db
from routes.task_routes import tasks_db
from routes.user_routes import users_db
from models.user import User

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    @app.route("/")
    def index():
        return "ToDo App is Running !"
    @app.route('/init-db/nr45ybimn498hnqhwj6wj4') # <-- استخدم أي نص سري وعشوائي هنا
    def init_db():
        db.create_all()
        return "Database has been successfully initialized!"
    app.register_blueprint(tasks_db, url_prefix = "/api")
    app.register_blueprint(users_db, url_prefix="/api/auth")
    return app

# --- This is the missing execution block ---
if __name__ == '__main__':
    # 1. Build the app by calling the factory
    app = create_app()
    # 2. Run the development server
    app.run(debug=True)
