## 🤖 Projeto

O  projeto bot-telegram-devs é um Bot desenvolvido em python para auxiliar os desenvolvedores na criação de seus telegram bots
com mais facilidade e produtividade.</br>
Seu funcionamento é dependente apenas de um banco de dados modelado especificamente para ele. Para isso, disponibilizamos um
[CRUD](https://github.com/JonathanGibimBorges/crud-bot-telegram) que irá alavancar a velocidade desse desenvolvimento, facilitando
o preenchimento desse banco com dados bem formatados e tratados.

## 🤔 Como rodar

- Faça o download desse repositório;
- Instale e ative sua virtualenv: `python -m venv venv`  `venv/scripts/activate` ou `venv/bin/activate`;
- Instale as dependências: `pip install -r requirements.txt`;
- Configure as variaveis de ambiente necessárias no caminho: `src/conf/.env`
- Configure o arquivo settings.py referenciando as variaveis de ambiente;
- Por fim, aproveite: `python core.py`;

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias e bibliotecas:

- [Python](https://docs.python.org/pt-br/3/index.html)
- [Telepot](https://telepot.readthedocs.io/en/latest/)
- [DotEnv](https://pypi.org/project/python-dotenv/)
- [Requests](https://requests.readthedocs.io/en/latest/)


## 📝 Observações

É preciso bastante cuidado com o preenchimento do campo scripts, ou seja, sua função do desenvolvedor. Pois apesar de sua capacidade de uso ser extremamente vasta, é perigosa!

- Caso ainda não tenha o banco de dados criado, execute: `python _database_.py`. Isso irá criá-lo no mesmo diretório do arquivo executado;

- Assista ao vídeo explicação para cessar outras dúvidas: [Vídeo](https://www.youtube.com/watch?v=40KhPfAmLWo)