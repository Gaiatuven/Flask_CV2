import sqlite3

def create_table():
    conn = sqlite3.connect('cv_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cv_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            education TEXT,
            experience TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_cv_data(name, email, education, experience):
    conn = sqlite3.connect('cv_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cv_data (name, email, education, experience) 
        VALUES (?, ?, ?, ?)
    ''', (name, email, education, experience))
    conn.commit()
    conn.close()

def fetch_latest_cv_data():
    conn = sqlite3.connect('cv_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cv_data ORDER BY id DESC LIMIT 1')
    data = cursor.fetchone()
    conn.close()

    if data:
        cv_data = {
            'name': data[1],
            'email': data[2],
            'education': data[3],
            'experience': data[4]
        }
    else:
        cv_data = {}

    return cv_data
