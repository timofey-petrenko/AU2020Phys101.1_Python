import cs50
from cs50 import SQL


db = SQL('sqlite:///list_of_classes.db') #работаем с SQLite через Python


student_name = input('Type in the full name (and the family name) of the student.\n') #получаем имя студента
list_of_subjects = input('Type in all the subjects this students has participated in, \
                         separate them by commmas.\n').split(',')#получаем список предметов, в которых он участвовал
for el in list_of_subjects:
    el.strip()


id = db.execute('INSERT INTO students (student) VALUES(?)', student_name) #добавляем его в таблицу студентов
for subject in list_of_subjects: #добавляем предметы в таблицу предметов, соотносяя со студентом
    id_class = db.execute('INSERT INTO classes (class_id, class) VALUES(?,?)', id, subject)
print('New data added successfully.')
