from services import listar_comandos
from tools.cep import consulta_cep
from tools.http_cats import get_photo


def processar_saida(comando, parametro=None):
    exec(comando.script, globals())

    if parametro:
        valores = script(parametro)
    else:
        valores = script()
    globals().pop('script')

    return comando.saida.format(**valores)
