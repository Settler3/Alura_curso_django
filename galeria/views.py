from django.shortcuts import render, get_object_or_404, redirect
from utils.validacao_login import login_required_message_and_redirect
from galeria.forms import FotografiaForms
from django.contrib import messages
from galeria.models import Fotografia, Categoria

@login_required_message_and_redirect(login_url='login', message='Efetue login')
def index(request):
    return render(request, 'galeria/index.html', {"cards": Fotografia.objects.order_by("-data_publicacao").filter(publicada=True)})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"foto": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_publicacao").filter(publicada=True)

    if "buscar" in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)
    return render(request, 'galeria/index.html', {"cards": fotografias})

@login_required_message_and_redirect(login_url='login', message='Efetue login')
def remover_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Foto deletada com sucesso')
    return redirect('index')

@login_required_message_and_redirect(login_url='login', message='Efetue login')
def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto editada com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao editar imagem')
            return redirect('editar_imagem')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

@login_required_message_and_redirect(login_url='login', message='Efetue login')
def nova_imagem(request):
    form = FotografiaForms()
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto adicionada com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao adicionar imagem')
            return redirect('nova_imagem')
    return render(request, 'galeria/nova_imagem.html', {'form': form})

@login_required_message_and_redirect(login_url='login', message='Efetue login')
def filtro(request, categoria):
    cat = Categoria.objects.get(nome=categoria)
    return render(request, 'galeria/index.html', {"cards": Fotografia.objects.order_by("-data_publicacao").filter(publicada=True, categoria=cat)})