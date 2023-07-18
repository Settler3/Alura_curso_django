from django.shortcuts import render

def index(request):
    return render(request, 'alura_space-projeto_front/index.html')

def imagem(request):
    return render(request, 'alura_space-projeto_front/imagem.html')