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
|__ docs/
|    |___images/
|          
│
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

2. Create virtual environment
bash
Copy
Edit
python -m venv .venv
3. Activate virtual environment
On Windows:

bash
Copy
Edit
.venv\Scripts\activate
On Linux/Mac:

bash
Copy
Edit
source .venv/bin/activate
4. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
5. Add your AviationStack API key
Rename .env.txt to .env

Inside .env, add:

ini
Copy
Edit
AVIATION_API_KEY=your_api_key_here
6. Apply migrations and run server
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Open browser at: http://127.0.0.1:8000/


🖼️ Screenshots
🏠 Home Page
![Homepage](docs/images/homepage1.png)

![homepage1](https://github.com/user-attachments/assets/f8454803-5722-49bb-a7bd-8e3b925336d2)


✈️ Search Flights
![Search_flightpage](docs/images/search_form.png)

![search_form](https://github.com/user-attachments/assets/12cd2549-9e42-42fe-a94d-2d817e9e4bd0)


✈️ Search Flights results
![Search_flight_resultpage](docs/images/flights_result.png)

![flights_result](https://github.com/user-attachments/assets/1d002961-55fb-4167-8226-9722e4d7dbf6)


📍 Airport Info
![Airportpage](docs/images/airport_info.png)

![airport_info](https://github.com/user-attachments/assets/ec9c482b-9431-4fc3-b806-7e024435e7e6)


📍 Airport Info result
![Airport_info_result_page](docs/images/airport_result.png)

![airport_result](https://github.com/user-attachments/assets/2a03dba4-ddb1-44b8-a35e-91c6865d2d77)


📌 Popular Routes
![Popular_routespage](docs/images/popular_routes.png)

![popular_routes](https://github.com/user-attachments/assets/5ebf2d20-1088-4a25-aed8-9f608b180135)


📝 Travel Tips
![Travel_tippage](docs/images/travel_tip.png)

![travel_tip](https://github.com/user-attachments/assets/14dd20dd-9ae1-4a10-b718-f475cd86fff2)


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

