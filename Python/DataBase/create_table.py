import cs50    #вот эту вот библиотеку https://cs50.readthedocs.io/libraries/cs50/python/ - она упрощает работу с SQLite через Python
from cs50 import SQL

open('list_of_classes.db', 'w').close() #создаем файл
db = SQL('sqlite:///list_of_classes.db') #работаем с ним через SQLite

db.execute('CREATE TABLE students (id INTEGER, student TEXT, PRIMARY KEY(id))') #создаем таблицу студентов
db.execute('CREATE TABLE classes (class_id INTEGER, class TEXT, FOREIGN KEY(class_id) REFERENCES  students(id))') #создаем таблицу предметов
