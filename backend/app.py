from flask import Flask
from flask_cors import CORS
from config import Config
from models.database import db
from routes.task_routes import tasks_db
from routes.user_routes import users_db
from models.user import User
from models.task import Task

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS for all routes
    CORS(app, origins=['http://localhost:3000', 'http://127.0.0.1:3000', 'http://localhost:3001', 'http://127.0.0.1:3001'])
    
    db.init_app(app)
    @app.route("/")
    def index():
        return "ToDo App is Running !"
    app.register_blueprint(tasks_db, url_prefix = "/api")
    app.register_blueprint(users_db, url_prefix="/api/auth")
    return app

# --- This is the missing execution block ---
if __name__ == '__main__':
    # 1. Build the app by calling the factory
    app = create_app()
    
    # 2. Create database tables
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
    
    # 3. Run the development server
    app.run(debug=True, host='0.0.0.0', port=5000)
