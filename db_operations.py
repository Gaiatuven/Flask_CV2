import json
import sqlite3

def create_table():
    with sqlite3.connect('cv_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cv_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone TEXT,
                address TEXT,
                education TEXT,
                skills TEXT,
                experience TEXT,
                projects TEXT
            )
        ''')

def insert_cv_data(name, email, phone, address, education, skills, experience, projects):
    with sqlite3.connect('cv_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO cv_data (name, email, phone, address, education, skills, experience, projects) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, address, education, skills, experience, projects))

def fetch_latest_cv_data():
    with sqlite3.connect('cv_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cv_data ORDER BY id DESC LIMIT 1')
        return cursor.fetchone()

def load_and_update_database_with_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    name = json_data.get('name', '')
    email = json_data.get('email', '')
    phone = json_data.get('phone', '')
    address = json_data.get('address', '')
    education = json_data.get('education', '')
    skills = json_data.get('skills', '')
    experience = json_data.get('experience', '')
    projects = json_data.get('projects', '')

    insert_cv_data(name, email, phone, address, education, skills, experience, projects)
