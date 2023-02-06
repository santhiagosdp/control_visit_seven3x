from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import visitante, visita
from datetime import date
from django.shortcuts import render


def home(requests):
    return render(requests, 'core/home.html')

#página form cadastro visita
@login_required
def cadastro(request):
    #BUSCAR VISITANTES PARA MODAL
    visitantes = visitante.objects.all()
    horas = date.today()
    atualizando = ""

    if request.method == 'POST': # se clicar em salvar, faz
        refresh = False
        print("refresh false 01")
        for item in visitantes:
            print("FOR ITEM INICIO")
            if item.nome == request.POST.get("name") and item.cidade == request.POST.get("city"):
                refresh = True
                print("refresh true 02")
                item.nome = request.POST.get("name")
                item.email = request.POST.get("mail")
                item.celular = request.POST.get("cel")
                item.fone = request.POST.get("fone")
                item.cep = request.POST.get("zip")
                item.endereco = request.POST.get("address")
                item.complemento = request.POST.get("complement")
                item.cidade = request.POST.get("city")
                item.estado = request.POST.get("state")
                item.save()
                
                cadastrarvisita = visita.objects.create(
                    usuario = request.user,
                    visitante = item,
                    descricao = request.POST.get("description"),
                )
                return render(request, 'core/cadastro.html', {"horas":horas, "visitantes":visitantes, "atualizando":atualizando})
                
        if refresh == False:
            print("IF refresh false 03")
            nome = request.POST.get("name")
            email = request.POST.get("mail")
            celular = request.POST.get("cel")
            fone = request.POST.get("fone")
            cep = request.POST.get("zip")
            endereco = request.POST.get("address")
            complemento = request.POST.get("complement")
            cidade = request.POST.get("city")
            estado = request.POST.get("state")
            descricao = request.POST.get("description")
            cadastrarvisitante = visitante.objects.create(
                usuario = request.user,
                nome = nome,
                email = email,
                celular = celular,
                fone = fone,
                cep = cep,
                endereco = endereco,
                complemento = complemento,
                cidade = cidade,
                estado = estado)
            
            cadastrarvisita = visita.objects.create(
                usuario = request.user,
                visitante = cadastrarvisitante,
                descricao = descricao,
            )
            visitantes = visitante.objects.all()
            return render(request, 'core/cadastro.html', {"horas":horas, "visitantes":visitantes, "atualizando":atualizando, "nome_pagina":"Cadastro de nova visita"})

    #SE BUSCAR VISITANTE NO MODAL
    busca = request.GET.get('search')
    if busca:
        print("IF BUSCAR 04")
        atualizando = visitante.objects.get(id = busca)
    print("ULTIMO RETURN")
    return render(request, 'core/cadastro.html', {"horas":horas, "visitantes":visitantes, "atualizando":atualizando,  "nome_pagina":"Cadastro de nova visita"})


@login_required
def relatorio(request):
    visitas = visita.objects.all()

    #SE CLICAR EM DELETAR VISITA
    busca = request.GET.get('delete')
    if busca:
        print(busca)
        deletar = visita.objects.get(id=busca)
        print(deletar)
        deletar.delete()

    #aparecer o indice de quantas visitas em #
    indice = 1
    for item in visitas:
        item.indice = indice
        indice = indice+1
    return render(request, 'core/relatorio.html', {"visitas":visitas, "nome_pagina":"Visitas e Demandas"})

@login_required
def contatos(request):
    pessoas = visitante.objects.all()

     #SE CLICAR EM DELETAR VISITA
    busca = request.GET.get('delete')
    if busca:
        print(busca)
        deletar = visitante.objects.get(id=busca)
        print(deletar)
        deletar.delete()

    #aparecer o indice de quantas visitas em #
    indice = 1
    for item in pessoas:
        item.indice = indice
        indice = indice+1

    return render(request, 'core/visitantes.html', {"pessoas":pessoas, "nome_pagina":"Visitantes"})
