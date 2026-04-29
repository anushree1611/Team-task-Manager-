from flask import Blueprint, request, redirect
from models import db, User

def is_admin(user_id):
    from models import User
    user = User.query.get(user_id)
    return user and user.role == "admin"

auth_bp = Blueprint('auth', __name__)


# ------------------------
# 📝 SIGNUP
# ------------------------
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.form if request.form else request.json

    # validation
    if not data.get('email') or not data.get('password'):
        return {"error": "Email & password required"}, 400

    # check existing user
    existing = User.query.filter_by(email=data['email']).first()
    if existing:
        return {"error": "User already exists"}, 400

    # create user
    user = User(
        name=data.get('name'),
        email=data['email'],
        password=data['password'],
        role=data.get('role', 'member')
    )

    db.session.add(user)
    db.session.commit()

    # redirect to login page
    return redirect('/')


# ------------------------
# 🔐 LOGIN
# ------------------------
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.form if request.form else request.json

    user = User.query.filter_by(email=data['email']).first()

    if user and user.password == data['password']:
        # redirect to dashboard after login
        return redirect('/dashboard')

    return {"error": "Invalid credentials"}, 401