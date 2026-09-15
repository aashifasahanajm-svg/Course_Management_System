# Course Management System

## Overview
A web-based Course Management System developed using HTML, CSS, JavaScript, Python, Django, Django REST Framework and SQLite.

## Features
- Add Course
- View Courses
- Edit Course
- Delete Course
- Search Course
- Input Validation
- REST API

## Technologies Used
- HTML
- CSS
- JavaScript
- Python
- Django
- Django REST Framework
- SQLite
- Postman

## API Endpoints
- GET /api/courses/
- POST /api/courses/
- GET /api/courses/{id}/
- PATCH /api/courses/{id}/
- DELETE /api/courses/{id}/

## How to Run

1. Open Command Prompt in the project folder.
2. Activate the virtual environment:
   venv\Scripts\activate.bat
3. Run the server:
   python manage.py runserver
4. Open:
   http://127.0.0.1:8000/

## Testing
The REST APIs were tested using Postman for GET, POST, PATCH and DELETE operations.