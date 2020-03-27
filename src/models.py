class Comando:
    def __init__(self, id_comando, comando, descricao, saida, script, ativo):
        self.id_comando = id_comando
        self.comando = comando
        self.descricao = descricao if descricao is not None else ''
        self.saida = saida
        self.script = script
        self.ativo = ativo

    def __repr__(self):
        return f'Comando({self.id_comando}, {self.comando}, {self.descricao}, {self.saida}, {self.script}, {self.ativo})'
