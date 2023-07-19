from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    return render(request, 'alura_space-projeto_front/index.html', {"cards": Fotografia.objects.order_by("-data_publicacao").filter(publicada=True)})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'alura_space-projeto_front/imagem.html', {"foto": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_publicacao").filter(publicada=True)

    if "buscar" in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)
    return render(request, 'alura_space-projeto_front/buscar.html', {"cards": fotografias})