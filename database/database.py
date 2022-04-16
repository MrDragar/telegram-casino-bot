from curses.ascii import US
import datetime
from email.policy import default

from peewee import Model, CharField, IntegerField, SqliteDatabase, TimeField, PrimaryKeyField, DoubleField, ForeignKeyField

sqlie_db = SqliteDatabase("database.db")

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = sqlie_db


class User(BaseModel):
    user_id = CharField()
    username = CharField()
    balance = DoubleField(default=0)
    language = CharField(default="en")


class Transaction(BaseModel):
    id = PrimaryKeyField()
    type_transaction = CharField()
    user = ForeignKeyField(User, backref="transaction")
    amount = DoubleField()
    time = TimeField()


class Main_information(BaseModel):
    id = PrimaryKeyField()
    user_count = IntegerField(default=0)
    input_money = DoubleField(default=0)
    output_money = DoubleField(default=0)


def init()-> None:
    """Формирует базу данных при запуске бота"""
    User.create_table()
    Transaction.create_table()
    Main_information.create_table()
    if Main_information.select().where(Main_information.id==0):
        main_information = Main_information.create()
        main_information.save()


def add_user(username: str, user_id: str, language: str) -> None:
    """Добавляет пользователя при его первом сообщении в базу данных"""
    if User.select().where(User.user_id==user_id).exists():
        return
    new_user = User.create(username=username, user_id=user_id, language=language)
    new_user.save()


def get_balance(user_id: str) -> str:
    """ Возвращает баланс пользователя"""
    user = User.select().where(User.user_id==user_id)[0]
    return user.balance