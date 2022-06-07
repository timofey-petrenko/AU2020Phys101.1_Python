from flask import Flask, render_template, request
import cs50
from cs50 import SQL

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")
db = SQL('sqlite:///students_languages.db') 

LANGUAGES = ['Spanish', 'German', 'French', 'Russian', 'Arabic', 'Mandarin', 'Japanese']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', languages=LANGUAGES)
    if request.method == 'POST':
        if not request.form.get('name'):
            return render_template('unsuccessful.html', message='Name is missing.')
        elif not request.form.get('language'):
            return render_template('unsuccessful.html', message='Choose your language of study.')
        elif request.form.get('language') not in LANGUAGES:
            return render_template('unsuccessful.html', message='The only languages available are those in the list.')
        else:
            id = db.execute('INSERT INTO language_students (student) VALUES(?)', request.form.get('name')) 
            db.execute('INSERT INTO language_subjects (class_id, class) VALUES(?,?)', id, request.form.get('language'))
            return render_template('successful.html', name=request.form.get('name'), language=request.form.get('language'))
