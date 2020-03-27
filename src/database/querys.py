from database.config import con
from database.utils.rows import rows_to_dict, row_to_dict
from contextlib import closing

sql_listar = "SELECT id_comando, comando, descricao, saida, script, ativo FROM comandos WHERE ativo = 1 ORDER BY comando"

sql_localizar = "SELECT id_comando, comando, descricao, saida, script, ativo FROM comandos WHERE comando = ? AND ativo = 1"


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_listar)
        comandos_bd = rows_to_dict(cursor.description, cursor.fetchall())
        return comandos_bd


def localizar(comando):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        a = cursor.execute(sql_localizar, (comando, ))
        row = cursor.fetchone()
        if row == None:
            raise ValueError
        
        return row_to_dict(cursor.description, row)
