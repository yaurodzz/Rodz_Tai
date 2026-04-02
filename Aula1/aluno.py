class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"ola meu nome é  {self.nome} e tenho {self.idade} anos."
        
    def maiordeidade(self):
        return self.idade >=18