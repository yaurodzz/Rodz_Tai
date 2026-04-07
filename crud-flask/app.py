
from flask import Flask, jsonify, request, render_template, redirect
from aluno import Aluno

app = Flask(__name__)

alunos = []

aluno1 = Aluno("Joao", 17)
aluno1.adicionar_nota(6)
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(8)

aluno2 = Aluno("Maria", 16)
aluno2.adicionar_nota(5)
aluno2.adicionar_nota(6)
aluno2.adicionar_nota(7)

aluno3 = Aluno("Rodz", 17)
aluno3.adicionar_nota(8)
aluno3.adicionar_nota(9)
aluno3.adicionar_nota(7)

alunos.append(aluno1)
alunos.append(aluno2)
alunos.append(aluno3)


@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html", alunos=alunos)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify([aluno.to_dict() for aluno in alunos])

@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    dados = request.get_json()
    novo_aluno = Aluno(dados["nome"], dados["idade"])

    novo_aluno.adicionar_nota(dados["nota1"])
    novo_aluno.adicionar_nota(dados["nota2"])
    novo_aluno.adicionar_nota(dados["nota3"])
    alunos.append(novo_aluno)

    return jsonify(novo_aluno.to_dict()), 201

@app.route("/remover/<int:id>")
def remover_aluno(id):
    global alunos
    alunos = [aluno for aluno in alunos if aluno.id != id]
    return redirect("/")
    
# Rota para carregar os dados de um aluno
@app.route("/editar/<int:id>")
def editar_aluno(id):
    aluno = next((aluno for aluno in alunos if aluno.id == id), None)
    if aluno:
        return render_template("editar.html", aluno=aluno)
    return redirect("/")

# Rota para atualizar um aluno
@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar_aluno(id):
    aluno = next((aluno for aluno in alunos if aluno.id == id), None)
    if aluno:
        aluno.nome = request.form["nome"]
        aluno.idade = int(request.form["idade"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)