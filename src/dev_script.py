from services import listar_comandos
from tools.cep import consulta_cep
from tools.http_cats import get_photo


def processar_saida(funcao, saida, *parametro):
    exec(funcao, globals())
    if parametro:
        parametros = script(*parametro)
    else:
        parametros = script()
    globals().pop('script')

    return saida.format(**parametros)


def executar(comando, parametro=None):
    if parametro is not None:
        return processar_saida(comando.script, comando.saida, parametro)    
    return processar_saida(comando.script, comando.saida)
