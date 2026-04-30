# 🚀 Team Task Manager

A full-stack web application to manage projects, assign tasks, and track team productivity with role-based access control.

---

## 🌐 Live Demo

👉 https://team-task-manager-production-b8ea.up.railway.app

---

## 📌 Overview

**Team Task Manager** is designed to help teams collaborate efficiently by organizing projects and tracking task progress in real-time.

Admins can manage projects and assign tasks, while team members can update task status and monitor deadlines.

---

## ✨ Key Features

### 🔐 Authentication

* Secure Signup & Login system
* Role-based access (Admin / Member)

### 📁 Project Management

* Create and manage multiple projects
* Assign tasks to team members

### ✅ Task Management

* Create tasks with deadlines
* Assign tasks to specific users
* Update task status (Pending / Completed)

### 📊 Dashboard

* Total tasks overview
* Completed tasks tracking
* Overdue tasks detection
* Real-time task status visualization

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Backend

* Python (Flask)
* Flask-SQLAlchemy

### Database

* PostgreSQL (Production - Railway)
* SQLite (Local Development)

### Deployment

* Railway
* Gunicorn (WSGI Server)

---

## 📂 Project Structure

```
team-task-manager/
│
├── Backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── project.py
│   │   ├── task.py
│   │
│   ├── templates/
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── dashboard.html
│   │
│   ├── static/
│   │   ├── style.css
│   │   ├── auth.css
│   │
│   ├── requirements.txt
│   ├── Procfile
│
├── README.md
```

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/anushree1611/Team-task-Manager-.git
cd Team-task-Manager-
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r Backend/requirements.txt
```

### 4️⃣ Run Application

```bash
cd Backend
python app.py
```

👉 Open in browser:

```
http://127.0.0.1:5000
```

---

## 🔐 Environment Variables

Create a `.env` file or set variables:

```
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

---

## 🚀 Deployment

Deployed on **Railway** using:

* Gunicorn server
* PostgreSQL database
* Environment variables

---

## 📸 Screenshots (Add Here)

* Login Page
* Signup Page
* Dashboard
* Task Assignment

---

## 🎯 Future Enhancements

* Email notifications
* Task comments & collaboration
* File attachments
* Advanced analytics dashboard

---

## 👩‍💻 Author

**Anushree**
📧 anushree.g886@gmail.com
🔗 https://github.com/anushree1611


---
