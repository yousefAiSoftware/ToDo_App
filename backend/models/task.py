from .database import db
from sqlalchemy import Integer, String, TIMESTAMP, Time, Boolean, Enum, ForeignKey

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(Integer , primary_key = True)
    user_id = db.Column(Integer , ForeignKey('users.id'), nullable = False)
    title = db.Column(String(255), nullable = False)
    task_description = db.Column(String(500), nullable = True)
    start_task_time = db.Column(TIMESTAMP, nullable = True)
    duration = db.Column(Time, nullable = True)
    due_date = db.Column(TIMESTAMP, nullable = True)
    is_completed = db.Column(Boolean , nullable=False, default = False)
    created_at = db.Column(TIMESTAMP, server_default = db.func.now())
    priority = db.Column(Enum("Important AND Urgent", "Important AND Not Urgent", "Not Important AND Urgent", "Not Important AND Not Urgent"), nullable = False, server_default = "Important AND Not Urgent")


    def to_dict(self):
        return {
            "id" : self.id,
            "user_id" : self.user_id,
            "title":self.title,
            "task_description":self.task_description,
            "start_task_time":self.start_task_time,
            "duration":self.duration,
            "due_date":self.due_date,
            "is_completed":self.is_completed,
            "created_at":self.created_at,
            "priority":self.priority
        }
