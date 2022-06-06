import cs50
from cs50 import SQL

open('list_of_classes.db', 'w').close()
db = SQL('sqlite:///list_of_classes.db')

db.execute('CREATE TABLE students (id INTEGER, student TEXT, PRIMARY KEY(id))')
db.execute('CREATE TABLE classes (class_id INTEGER, class TEXT, FOREIGN KEY(class_id) REFERENCES  students(id))')
