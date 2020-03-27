from models import Comando
from database.querys import listar, localizar


def listar_comandos():
    comandos = []
    comandos_bd = listar()
    for comando_bd in comandos_bd:
        comandos.append(Comando(comando_bd['id_comando'], comando_bd['comando'], comando_bd['descricao'], comando_bd['saida'], 
                                comando_bd['script'], comando_bd['ativo']))
    return comandos


def localizar_comando(comando):
    comando_bd = localizar(comando)
    return Comando(comando_bd['id_comando'], comando_bd['comando'], comando_bd['descricao'], comando_bd['saida'], comando_bd['script'],
                   comando_bd['ativo'])
