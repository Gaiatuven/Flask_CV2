import sqlite3
from flask import Flask, render_template
from db_operations import create_table, fetch_latest_cv_data, load_and_update_database_with_json

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the index page with CV data.

    Returns:
    flask.Response: The rendered HTML template.
    """
    return render_template("index.html")

@app.route('/cv')
def cv():
    # Fetch the latest CV data from the database
    cv_data = fetch_latest_cv_data()
    return render_template('cv.html', cv_data=cv_data)

if __name__ == '__main__':
    create_table()
    load_and_update_database_with_json('cv_data.json')
    app.run(debug=True)
