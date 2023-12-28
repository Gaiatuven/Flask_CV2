from flask import Flask, render_template, request
from db_operations import create_table, insert_cv_data, fetch_latest_cv_data

app = Flask(__name__)

create_table()  # Create SQLite table on application startup

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv', methods=['GET', 'POST'])
def cv():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        education = request.form['education']
        experience = request.form['experience']

        insert_cv_data(name, email, education, experience)

    cv_data = fetch_latest_cv_data()

    return render_template('cv.html', cv_data=cv_data)

if __name__ == '__main__':
    app.run(debug=True)
