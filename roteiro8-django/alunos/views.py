import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Aluno

# Tela inicial (Renderiza index.html)
def pagina_inicial(request):
    return render(request, 'index.html')

@csrf_exempt
def api_alunos(request):
    # GET: Listar todos os alunos
    if request.method == 'GET':
        lista_alunos = Aluno.objects.all()
        dados = [aluno.to_dict() for aluno in lista_alunos]
        return JsonResponse(dados, safe=False, status=200)
    # POST: Criar novo aluno
    elif request.method == 'POST':
        payload = json.loads(request.body)
        nome = payload.get('nome')
        idade = payload.get('idade')
        media = payload.get('media', 8.5) # Valor padrão

        if not nome or not isinstance(idade, int):
            return JsonResponse({"erro": "Dados inválidos."}, status=400)
        
        novo = Aluno.objects.create(nome=nome, idade=idade, nota=media)
        return JsonResponse(novo.to_dict(), status=201)
    

@csrf_exempt
def api_alunos_detalhe(request, id):
    # DELETE: Remover aluno
    if request.method == 'DELETE':
        try:
            aluno = Aluno.objects.get(id=id)
            aluno.delete()
            return JsonResponse(
                {"mensagem": "Removido com sucesso"}, status=200
            )
        except Aluno.DoesNotExist:
            return JsonResponse({"erro": "Nao encontrado"}, status=404)