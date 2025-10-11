from flask import Blueprint , jsonify , request
from models.task import Task
from models.database import db
from utils.auth_helper import token_required
from datetime import datetime

tasks_db = Blueprint("tasks",__name__)

def parse_datetime(date_string):
    """Convert datetime string to Python datetime object"""
    if not date_string:
        return None
    try:
        # Handle HTML datetime-local format: 2025-10-11T12:16
        return datetime.fromisoformat(date_string.replace('T', ' '))
    except ValueError:
        try:
            # Handle other common formats
            return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return None

@tasks_db.route("/tasks", methods = ["POST", "GET"])
@token_required
def handle_tasks(current_user):
    if request.method == "POST":
        task_data = request.get_json()
        if not task_data or not "title" in task_data:
            return jsonify({"error":"Missing data"}),400
        
        # Parse datetime fields
        start_task_time = parse_datetime(task_data.get("start_task_time"))
        due_date = parse_datetime(task_data.get("due_date"))
        duration = task_data.get("duration")  # Keep as string for Time field
        
        # Check if at least one time-related field is provided (but make it optional)
        # if not start_task_time and not duration and not due_date:
        #     return jsonify({'error': 'At least one of start_task_time, or duration, or due_date is required'}), 400
        
        new_task = Task(
            user_id = current_user.id,
            title=task_data["title"],
            task_description=task_data.get("task_description"),
            start_task_time=start_task_time,
            duration=duration,
            due_date=due_date,
            priority=task_data.get("priority", "Important AND Not Urgent"),
            )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()),201
    if request.method == "GET":
        all_tasks = Task.query.filter_by(user_id=current_user.id).all()
        all_tasks_dict = []
        for task in all_tasks:
            all_tasks_dict.append(task.to_dict()) # -> = [task.to_dict() for task in all_tasks]
        return jsonify(all_tasks_dict)


@tasks_db.route("/tasks/<int:task_id>", methods=["GET", "PUT", "DELETE"])
@token_required
def handle_single_task(current_user, task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        return jsonify({"error": "Unauthorized access to this resource"}), 403
    if request.method == "GET":
        return jsonify(task.to_dict())
    elif request.method == "PUT":
        data = request.get_json()
        task.title = data.get('title', task.title)
        task.is_completed = data.get('is_completed', task.is_completed)
        db.session.commit()
        return jsonify(task.to_dict())
    elif request.method == "DELETE":
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task Deleted Successfully"})
