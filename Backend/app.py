from flask import Flask, render_template
from config import Config
from models import db, Task
from datetime import datetime

from routes.auth import auth_bp
from routes.project import project_bp
from routes.task import task_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ✅ Create tables safely (runs once at startup)
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print("DB INIT ERROR:", e)

# ✅ Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(project_bp)
app.register_blueprint(task_bp)

# 🔐 LOGIN PAGE (homepage)
@app.route('/')
def home():
    return render_template('login.html')


# 📝 SIGNUP PAGE
@app.route('/signup-page')
def signup_page():
    return render_template('signup.html')


# 📊 DASHBOARD (safe DB handling)
@app.route('/dashboard')
def dashboard():
    try:
        tasks = Task.query.all()
        total = len(tasks)
        completed = Task.query.filter_by(status="done").count()
        overdue = Task.query.filter(
            Task.due_date < datetime.utcnow(),
            Task.status != "done"
        ).count()
    except Exception as e:
        print("DB ERROR:", e)
        tasks = []
        total = completed = overdue = 0

    return render_template(
        "dashboard.html",
        tasks=tasks,
        total=total,
        completed=completed,
        overdue=overdue
    )