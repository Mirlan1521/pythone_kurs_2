from peewee import *

db = SqliteDatabase('Popytka.db')


class Teacher(Model):
    name = CharField()
    surname = CharField()
    lesson = CharField()

    class Meta:
        database = db


class Apprentice(Model):
    name = ForeignKeyField(, backref='Teacher')
    surname = CharField()
    course = IntegerField()

    class Meta:
        database = db


db.connect()

db.create_tables([Teacher, Apprentice])
