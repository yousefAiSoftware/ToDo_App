from flask import Blueprint , jsonify , request
from models.task import Task
from models.database import db
from utils.auth_helper import token_required

tasks_db = Blueprint("tasks",__name__)




@tasks_db.route("/tasks", methods = ["POST", "GET"])
@token_required
def handle_tasks(current_user):
    if request.method == "POST":
        task_data = request.get_json()
        if not task_data or not "title" in task_data:
            return jsonify({"error":"Missing data"}),400
        if ("start_task_time" not in task_data) and ("duration" not in task_data) and ("due_date" not in task_data):
            return jsonify({'error': 'At least one of start_task_time, or duration, or due_date is required'}), 400
        new_task = Task(
            user_id = current_user.id, # Have to develop
            title=task_data["title"],
            task_description=task_data.get("task_description"),
            start_task_time=task_data.get("start_task_time"),
            duration=task_data.get("duration"),
            due_date=task_data.get("due_date"),
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
