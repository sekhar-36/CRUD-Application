# Django Company CRUD Application

This is a Django application that provides CRUD (Create, Read, Update, Delete) functionalities for managing company records.

## Table of Contents
Installation

Usage

Features

Technologies

Contributing

## Installation
Prerequisites
Python 3.7+

Django 3.0+

pip (Python package installer)

## Steps
1. Clone the repository:

    git clone https://github.com/sekhar-36/django-company-crud.git
   
    cd django-company-crud
   
2. Create and activate a virtual environment:

   python -m venv venv
   
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install the dependencies:

    pip install -r requirements.txt

4. Apply the migrations:

    python manage.py makemigrations

   python manage.py migrate

5. Run the development server:

   python manage.py runserver

6. Open your browser and navigate to http://127.0.0.1:8000 to access the application.

## Usage

Admin Panel

1. Create a superuser to access the admin panel:

   python manage.py createsuperuser

2. Access the admin panel at http://127.0.0.1:8000/admin and log in with the superuser credentials.

## CRUD Operations

Create: Use the "Add Company" button to add a new company record.

Read: View a list of all company records on the main page.

Update: Click on a company record to edit its details.

Delete: Use the delete button next to a company record to remove it.

## Features
Add new company records.

View a list of all companies.

Edit existing company details.

Delete company records.

Admin panel for managing company records and users.

## Technologies
Backend: Django

Database: SQLite (default, can be configured for PostgreSQL, MySQL, etc.)

Frontend: HTML, CSS, JavaScript (Bootstrap for styling)

## Contributing
1. Fork the repository.

2. Create a new branch (git checkout -b feature/your-feature).

3. Commit your changes (git commit -m 'Add some feature').

4. Push to the branch (git push origin feature/your-feature).

5. Create a new Pull Request.









