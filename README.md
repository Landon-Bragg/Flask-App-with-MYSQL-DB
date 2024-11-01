# Flask App with MySQL Database
This repository contains a Flask application connected to a MySQL database. The app showcases CRUD operations and integrates HTML templates for the front end, making it ideal for learning and experimenting with full-stack development principles. As a data science student, I developed this project to deepen my understanding of backend operations and how they interface with a database, as well as how data can be visualized in a front-end environment.

## Features
Flask Web Framework: Serves as the foundation for building and running the web application.
MySQL Database: Manages the data with tables for different entities.
HTML Templates: Provides a user-friendly interface, featuring templates for various views.
CRUD Functionality: Users can create, read, update, and delete entries in the database.
Technologies Used
Python: Main programming language for backend operations.
Flask: Lightweight web application framework.
MySQL: Database system for storing and retrieving data.
HTML/CSS: Front-end templates for rendering the user interface.
Installation
Prerequisites
Python 3.x
MySQL
pip (Python package installer)
Setup Steps
Clone the Repository:

bash
Copy code
git clone git@github.com:Landon-Bragg/Flask-App-with-MYSQL-DB.git
cd Flask-App-with-MYSQL-DB
Set Up a Virtual Environment (optional, but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Configure MySQL Database:

Create a MySQL database for the app.
Update the database connection information in the application (typically in a config file or within index.py).
Run Database Migrations: This application may include SQL scripts for setting up tables. Run these to initialize the database:

bash
Copy code
mysql -u username -p database_name < path/to/sql_script.sql
Run the Application:

bash
Copy code
flask run
The app will be accessible at http://127.0.0.1:5000.

Usage
Home Page: Provides access to the main sections of the application.
Database Operations: Pages allow adding, viewing, editing, and deleting entries from the MySQL database.
HTML Pages: Templates for displaying data and forms in a structured layout.
