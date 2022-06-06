import cs50
from cs50 import SQL

open('list_of_classees.db', 'w').close()
db = SQL('sqlite:///exams.db')

db.execute('CREATE TABLE students (id INTEGER, student TEXT, PRIMARY KEY(id))')
db.execute('CREATE TABLE classes (class_id INTEGER, class TEXT, FOREIGN KEY(class_id) REFERENCES  students(id))')
