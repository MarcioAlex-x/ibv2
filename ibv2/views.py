from django.shortcuts import render, get_object_or_404
from . import models

def index(request):
    ultimo_destaque = models.Destaque.objects.latest('id')
    destaques = models.Destaque.objects.order_by('-id').all()
    publicacoes = models.Publicacoes.objects.order_by('-id').all()
    programacao = models.Programacao.objects.order_by('-id').all()
    eventos = models.Eventos.objects.order_by('-id').all()
    classificados = models.Classificados.objects.order_by('-id').all()
    return render(request,'index.html',{'destaques':destaques,'publicacoes':publicacoes,'programacao':programacao,'eventos':eventos,'classificados':classificados, 'ultimo_destaque':ultimo_destaque})

def classificados(request):
    classificados = models.Classificados.objects.order_by('-id').all()
    return render(request, 'classificados.html', {'classificados':classificados})

def contato(request):
    return render(request, 'contato.html')

def destaque(request, id):
    destaques=models.Destaque.objects.order_by('-id').all()
    destaque = get_object_or_404(models.Destaque, id=id)
    return render(request, 'destaque.html', {'destaque':destaque, 'destaques':destaques})

def eventos(request):
    eventos = models.Eventos.objects.all()
    return render(request, 'eventos.html', {'eventos':eventos})

def programacao(request):
    programacoes = models.Programacao.objects.all()
    return render(request, 'programacao.html',{'programacoes':programacoes})

def publicacao(request, id):
    publicacao = get_object_or_404(models.Publicacoes, id=id)
    return render(request, 'publicacao.html',{'publicacao':publicacao})

def sobre(request):
    return render(request, 'sobre.html')

