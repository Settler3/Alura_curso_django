from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    return render(request, 'alura_space-projeto_front/index.html', {"cards": Fotografia.objects.all()})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'alura_space-projeto_front/imagem.html', {"foto": fotografia})