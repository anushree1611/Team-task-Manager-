from flask import Blueprint, request, redirect
from models import db, Task, User
from datetime import datetime

task_bp = Blueprint('task', __name__)

# check admin
def is_admin(user_id):
    user = User.query.get(user_id)
    return user and user.role == "admin"


# ✅ Create Task (Admin only)
@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.form if request.form else request.json

    if not is_admin(int(data['created_by'])):
        return {"error": "Only admin can assign tasks"}, 403

    task = Task(
        title=data['title'],
        project_id=int(data['project_id']),
        assigned_to=int(data['assigned_to']),
        due_date=datetime.strptime(data['due_date'], "%Y-%m-%d"),
        status="todo"
    )

    db.session.add(task)
    db.session.commit()

    return redirect('/dashboard')


# ✅ Update Task (Only assigned user)
@task_bp.route('/tasks/<int:id>', methods=['POST', 'PUT'])
def update_task(id):
    data = request.form if request.form else request.json

    task = Task.query.get(id)

    if not task:
        return {"error": "Task not found"}, 404

    if task.assigned_to != int(data['user_id']):
        return {"error": "You can only update your own task"}, 403

    task.status = data['status']

    if task.status == "done":
        task.completed_at = datetime.utcnow()

    db.session.commit()

    return redirect('/dashboard')