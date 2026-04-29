from flask import Blueprint, request
from models import db, Project, ProjectMember, User

project_bp = Blueprint('project', __name__)

def is_admin(user_id):
    user = User.query.get(user_id)
    return user and user.role == "admin"


@project_bp.route('/projects', methods=['POST'])
def create_project():
    data = request.json

    if not is_admin(data['admin_id']):
        return {"error": "Only admin can create project"}, 403

    project = Project(
        title=data['title'],
        admin_id=data['admin_id']
    )

    db.session.add(project)
    db.session.commit()

    return {"message": "Project created"}