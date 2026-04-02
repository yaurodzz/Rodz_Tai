from aluno import Aluno

alunos = [
    Aluno("joao", 18),
    Aluno("pedro", 16),
    Aluno("maria", 17)
]

for aluno in alunos:
    print(aluno.apresentar())
    if aluno.maiordeidade():
        print(f"{aluno.nome} é maior de idade")