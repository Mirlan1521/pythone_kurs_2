import sqlite3


class Product:

    def __init__(self):
        self.connection = sqlite3.connect('HW.sqlite3')
        pass

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table products(id integer, name text);')
        except sqlite3.OperationalError:
            print("Таблица уже создана")
        self.connection.commit()

    def insert(self, id, name):
        cursor = self.connection.cursor()
        cursor.execute("insert into products values(?, ?)", (id, name))
        self.connection.commit()
        print("Выполнен Insert")

    def update(self, id, name=None):
        cursor = self.connection.cursor()
        cursor.execute(f"update products set name = 'Milk' where id = {id}")
        self.connection.commit()
        print("Выполнен Update")

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"delete from products where id = {id}")
        self.connection.commit()
        print("Выполнен Delete")


product = Product()
product.create_table()
product.insert(1, "Sahar")
product.update(2)
product.delete(1)
