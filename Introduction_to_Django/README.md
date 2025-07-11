# LibraryProject

This is the initial setup of a Django web application, created as part of the **Introduction to Django** module for the `Alx_DjangoLearnLab`. This project lays the foundation for developing full Django applications.

---

## 📌 Project Overview

The `LibraryProject` is a basic Django project aimed at understanding:
- How to install and configure Django
- How to create a new Django project
- How to run the development server
- The roles of key Django files (`manage.py`, `settings.py`, `urls.py`)

---

## 🧱 Project Structure

LibraryProject/
├── LibraryProject/
│ ├── init.py
│ ├── settings.py # Configuration file
│ ├── urls.py # Root URL declarations
│ ├── wsgi.py # WSGI entry point
│ └── asgi.py # ASGI entry point
├── manage.py # CLI tool to manage the project
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install django

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser. You should see the Django welcome page.

## 📚 Key Files Explained

manage.py: Entry point for managing the project (migrations, server, etc.)

settings.py: Holds project configuration like installed apps, database settings, etc.

urls.py: Controls how URLs are routed to views.

wsgi.py and asgi.py: Entry points for different deployment setups.

## 📎 Next Steps
Add a Django app (e.g., library) using:

python manage.py startapp library

## 🛠 Tech Stack
Python

Django

## ✍️ Author
Mohammed Naji Abdullah
ALX Django Learning Lab
