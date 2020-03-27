import telepot
import re
from conf.settings import TELEGRAM_TOKEN
from services import localizar_comando
from dev_script import executar


class ParameterError(Exception): ...

class RequiredParameterError(Exception): ...

class UserParameterError(Exception): ...

class DeveloperParameterError(Exception): ...


def send(chat_id, resposta):
    if 'photo' in resposta:
            BOT.sendPhoto(chat_id, resposta[5:])
    else:
        BOT.sendMessage(chat_id, resposta)


def search_param(script):
    if ',' in script.split(':')[0]:
        raise DeveloperParameterError
    return re.search('script[(][a-z_][a-z_]*[)]', script)


def validate(chat_id, mensagem, *parametro):
    try:
        print(mensagem)
        comando = localizar_comando(mensagem)

        if comando.script is not None:
            if not search_param(comando.script):
                if parametro:
                    raise ParameterError
                return executar(comando)

            if len(parametro) > 1:
                raise UserParameterError

            if search_param(comando.script):
                if not parametro:
                    raise RequiredParameterError
                return executar(comando, *parametro)
            
        return comando.saida

    except ValueError:
        return 'Desculpe, mas não sei como responder a isso.'

    except ParameterError:
        return f'Desculpe, mas este comando não recebe nenhum parâmetro. Recebi {list(parametro)}'

    except RequiredParameterError:
        return 'Este comando necessita de um parâmetro, porém você não me enviou.'
    
    except UserParameterError:
        return f'Por favor, certifique-se de que apenas um parâmetro seja enviado. Recebi {list(parametro)}'

    except DeveloperParameterError:
        funcao = comando.script.split(':')[0]
        print(f'{DeveloperParameterError.__name__}: A nomenclatura de sua função no campo script deve ser [def script()] ou [def script(args)]. No máximo um parâmetro!')
        print(f'Encontrei [{funcao}]')
        return f'Desculpe, esse recurso está em manutenção.'
        
    except NameError:
        nome_funcao = comando.script.split('(')[0][4:]
        print(f'{NameError.__name__}: O nome da função no campo script deve ser [script]! Encontrei [{nome_funcao}].')
        print('Caso o nome esteja correto, o problema está em seu script. Verifique as chamadas e funções internas desse script.')
        return 'Desculpe, esse recurso está temporariamente inativo.'

    except SyntaxError:
        print(f'{SyntaxError.__name__}: Existe algo de errado em seu [script]! \n{comando.script}')
        return 'Desculpe, esse recurso está temporariamente bloqueado.'


def handler(msg):
    chat_id = msg['chat']['id']
    mensagem = msg['text'].split()
    print(mensagem)
    resposta = validate(chat_id, *mensagem)
    send(chat_id, resposta)


BOT = telepot.Bot(TELEGRAM_TOKEN)

if __name__ == '__main__':
    print('pressione CTRL + C para desativar o bot.')
    BOT.message_loop(handler)  
    while True:
        ...
