# ✈️ Airline Reservation System (Django Project)

A web-based airline reservation system built using **Django**, **Python**, **HTML/CSS**, and **MySQL**. The project fetches live flight data via the AviationStack API and provides useful features for flight search, airport info, travel routes, and travel tips.

---

## 📁 Project Structure

FINALPROJ/
├── .venv/                      # Virtual environment (auto-generated)
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   └── pyvenv.cfg
│
├── finalproj/                 # Main Django project folder
│   └── ... (settings.py, urls.py etc.)
│___ docs/
|     |___images/
|
├── myapp/                     # Django app
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │   └── images/
│   │       ├── airport.jpeg
│   │       ├── home.jpeg
│   │       ├── search_form.jpg
│   │       └── travel.jpeg
│   │
│   ├── templates/
│   │   └── myapp/
│   │       ├── home.html
│   │       ├── flights.html
│   │       ├── results.html
│   │       ├── popular_routes.html
│   │       ├── airport_info.html
│   │       ├── airport_result.html
│   │       └── travel_tip.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── .env.txt                   # 🔴 Rename to .env (to store secrets like API keys)
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django command-line tool
└── requirements.txt           # List of installed packages
|__ README.md                  #  Setup and documentation

---

## 🚀 Features

- 🔎 **Live Flight Search** using AviationStack API  
- 🧭 **Popular Travel Routes** in India  
- 🛫 **Airport Info Lookup** via MySQL database  
- 🧳 **Travel Tips Page** for users  
- 🖼️ Integrated with relevant images for better UI

---

## 🔧 Setup Instructions

### 1. Clone the project
```bash
git clone <your-repo-url>
cd FINALPROJ
_ _ _

### 2. Create virtual environment
python -m venv .venv
_ _ _

3. Activate virtual environment
- On Windows:
 .venv\Scripts\activate
_ _ _

- On Linux/Mac:
 source .venv/bin/activate
_ _ _

4. Install dependencies
pip install -r requirements.txt
_ _ _

5. Add your AviationStack API key
Rename .env.txt to .env
Inside .env, add:
AVIATION_API_KEY=your_api_key_here
_ _ _

6. Apply migrations and run server
python manage.py migrate
python manage.py runserver
Open browser at: http://127.0.0.1:8000/

---

📦 Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS
Database:  MySQL
API: AviationStack API

---

🙋‍♀️ Author
👩‍💻 Project by Shruti 
📚 Student Developer | Django Enthusiast

---

⚠️ Notes
🔐 Keep your .env file secret – never share your real API key!

---

✅ Tested with Django 4.x and Python 3.x

---

