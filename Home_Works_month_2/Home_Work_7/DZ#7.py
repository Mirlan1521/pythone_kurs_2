import sqlite3


class Author:

    def __init__(self):
        self.connection = sqlite3.connect('HW7.sqlite3')

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table author('
                           'id integer primary key unique, name text, surname text, work_place text);')
        except sqlite3.OperationalError:
            print("Таблица уже создана")
        self.connection.commit()

    def insert(self, id, name, surname, work_place):
        cursor = self.connection.cursor()
        cursor.execute("insert into author values(?, ?, ?, ?)", (id, name, surname, work_place))
        self.connection.commit()
        print("Выполнен Insert")

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from author where id = 3")
        j = cursor.fetchall()
        print(j)
        self.connection.commit()

class Post:
    def __init__(self):
        self.connection = sqlite3.connect('HW7.sqlite3')
        pass

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table post '
                           '('
                           'id integer primary key unique, '
                           'tittle text, '
                           'description text, '
                           'date text, author_id integer, foreign key(author_id) references author(id));')
        except sqlite3.OperationalError:
            print("Таблица уже создана2")
        self.connection.commit()

    def insert(self, id, tittle, description, date, author_id):
        cursor = self.connection.cursor()
        cursor.execute("insert into post values(?, ?, ?, ?, ?)", (id, tittle, description, date, author_id))
        self.connection.commit()
        print("Выполнен Insert")

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from post where author_id = 2")
        h = cursor.fetchall()
        print(h)
        self.connection.commit()

    def join(self):
        cursor = self.connection.cursor()
        cursor.execute("select post.tittle, post.description, author.name "
                       "from post "
                       "inner join author author on author.id = post.author_id")
        self.connection.commit()



sozdat_authora = Author()
sozdat_post = Post()
#sozdat_authora.create_table()
#sozdat_post.create_table()
# sozdat_authora.insert(1, "Nurbek", "Tashmatov", "Azattyk")
# sozdat_authora.insert(2, "Mirbek", "Eshmatov", "Kabarlar")
# sozdat_authora.insert(3, "Temirbek", "Kashmatov", "Kaktusmedia")
# sozdat_post.insert(1, "Pogoda", "Jarishe", "20.05.2020", 1)
# sozdat_post.insert(2, "Leto", "Kanikuly", "01.07.2020", 1)
# sozdat_post.insert(3, "Economica", "Konets micro economice", "12.12.2019", 2)
# sozdat_post.insert(4, "Voina", "Vtoroia mirovaia voina", "09.05.2020", 2)
# sozdat_post.insert(5, "Comics", "Flash", "01.01.2021", 3)
# sozdat_post.insert(6, "Films", "Superman", "23.02.2021", 3)
#sozdat_post.select()
#sozdat_authora.select()
