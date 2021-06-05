import sqlite3


class Teacher:

    def __init__(self):
        self.connection = sqlite3.connect('HW8.sqlite3')

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table teacher('
                           'id integer primary key unique, name text, surname text, lesson text);')
        except sqlite3.OperationalError:
            print("Таблица уже создана")
        self.connection.commit()

    def insert(self, id, name, surname, lesson):
        cursor = self.connection.cursor()
        cursor.execute("insert into teacher values(?, ?, ?, ?)", (id, name, surname, lesson))
        self.connection.commit()
        print("Выполнен Insert")

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from teacher where id = 3")
        j = cursor.fetchall()
        print(j)
        self.connection.commit()


class Apprentice:
    def __init__(self):
        self.connection = sqlite3.connect('HW8.sqlite3')
        pass

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table apprentice '
                           '('
                           'id integer primary key unique, '
                           'name text, '
                           'surname text, '
                           'klass text, teacher_id integer, foreign key(teacher_id) references teacher(id));')
        except sqlite3.OperationalError:
            print("Таблица уже есть")
        self.connection.commit()

    def insert(self, id, name, surname, klass, teacher_id):
        cursor = self.connection.cursor()
        cursor.execute("insert into apprentice values(?, ?, ?, ?, ?)", (id, name, surname, klass, teacher_id))
        self.connection.commit()
        print("Выполнен Insert2")

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from post where teacher_id = 2")
        h = cursor.fetchall()
        print(h)
        self.connection.commit()


class TimeTable:
    def __init__(self):
        self.connection = sqlite3.connect('HW8.sqlite3')
        pass

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table timetable '
                           '('
                           'teacher_id integer, '
                           'apprentice_id integer, '
                           'primary key(teacher_id, apprentice_id),'
                           'foreign key(teacher_id) references teacher(id),'
                           'foreign key(apprentice_id) references apprentice(id))')
        except sqlite3.OperationalError:
            print("Таблица  есть смотри код")
        self.connection.commit()

    def insert(self, teacher_id, apprentice_id):
        cursor = self.connection.cursor()
        cursor.execute("insert into timetable values(?, ?)", (teacher_id, apprentice_id))
        self.connection.commit()
        print("Выполнен Insert3")

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from timetable where apprentice_id = 6")
        l = cursor.fetchall()
        print(l)
        self.connection.commit()

    def superjoin(self):
        cursor = self.connection.cursor()
        cursor.execute("select teacher.surname, teacher.lesson, apprentice.name from teacher "
                       "inner join timetable timetable on teacher.id = timetable.teacher_id "
                       "inner join apprentice apprentice on apprentice.id = timetable.apprentice_id")
        z = cursor.fetchall()
        print(z)
        self.connection.commit()


sozdat_teacher = Teacher()
sozdat_apprentice = Apprentice()
sozdat_teacher.create_table()
sozdat_apprentice.create_table()
sozdat_timetable = TimeTable()
sozdat_timetable.create_table()
# sozdat_teacher.insert(1, "Maksat", "Aliev", "Matematika")
# sozdat_teacher.insert(2, "Mirbek", "Eshmatov", "Fizkultura")
# sozdat_teacher.insert(3, "Ruslan", "Kadyrov", "English")
# sozdat_apprentice.insert(1, "Tashmat", "Tashmatov", "8", 1)
# sozdat_apprentice.insert(2, "Eshmat", "Eshmatov", "8", 1)
# sozdat_apprentice.insert(3, "Ailin", "Osmonkulova", "10", 2)
# sozdat_apprentice.insert(4, "Alina", "Kanymetova", "10", 2)
# sozdat_apprentice.insert(5, "Altynai", "Chekirova", "9", 3)
# sozdat_apprentice.insert(6, "Elina", "Kanatova", "9", 3)
# sozdat_timetable.insert(1, 2)
# sozdat_timetable.insert(1, 1)
# sozdat_timetable.insert(2, 3)
# sozdat_timetable.insert(2, 4)
# sozdat_timetable.insert(3, 5)
# sozdat_timetable.insert(3, 6)
# sozdat_timetable.insert(1, 6)
#sozdat_timetable.superjoin()
