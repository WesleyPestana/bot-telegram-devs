import sqlite3
from conf.settings import DATABASE_PATH
from contextlib import closing

sql_create = '''CREATE TABLE IF NOT EXISTS comandos (
id_comando INTEGER PRIMARY KEY AUTOINCREMENT,
comando VARCHAR(20) NOT NULL UNIQUE,
saida VARCHAR(300) NOT NULL,
script VARCHAR(800),
ativo BOOLEAN NOT NULL
);
'''


def con():
    return sqlite3.connect(DATABASE_PATH)


def criar_bd():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.executescript(sql_create)
        connection.commit()
