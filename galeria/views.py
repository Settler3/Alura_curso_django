from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from galeria.models import Fotografia

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue login')
        return redirect('login')
    else:
        return render(request, 'galeria/index.html', {"cards": Fotografia.objects.order_by("-data_publicacao").filter(publicada=True)})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"foto": fotografia})

@login_required
def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_publicacao").filter(publicada=True)

    if "buscar" in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)
    return render(request, 'galeria/buscar.html', {"cards": fotografias})