from flask import Flask, jsonify, request, render_template, redirect
from aluno import Aluno

app = Flask(__name__)

alunos = []

@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html", alunos=alunos)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify([aluno.to_dict() for aluno in alunos])

@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    nome_form = request.form["nome"]
    idade_form = int(request.form["idade"])

    nota1 = float(request.form["nota1"])
    nota2 = float(request.form["nota2"])
    nota3 = float(request.form["nota3"])

    novo_aluno = Aluno(nome_form, idade_form)

    novo_aluno.adicionar_nota(nota1)
    novo_aluno.adicionar_nota(nota2)
    novo_aluno.adicionar_nota(nota3)

    alunos.append(novo_aluno)

    aluno_existente = None
    for a in alunos:
        if a.nome == nome_form:
            aluno_existente = a
            break

    if aluno_existente:
        aluno_existente.idade = idade_form
        aluno_existente.notas = [nota1, nota2, nota3]
    else:
        novo_aluno = Aluno(nome_form, idade_form)
        novo_aluno.adicionar_nota(nota1)
        novo_aluno.adicionar_nota(nota2)
        novo_aluno.adicionar_nota(nota3)
        alunos.append(novo_aluno)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)