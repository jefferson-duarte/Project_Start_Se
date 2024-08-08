from django.contrib import messages
from django.contrib.messages import constants
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from .models import Empresas


def cadastrar_empresa(request):
    if request.method == 'GET':
        tempo_existencia = Empresas.tempo_existencia_choices
        areas = Empresas.area_choices

        context = {
            'tempo_existencia': tempo_existencia,
            'areas': areas,
        }

        return render(request, 'cadastrar_empresa.html', context)

    elif request.method == "POST":
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        site = request.POST.get('site')
        tempo_existencia = request.POST.get('tempo_existencia')
        descricao = request.POST.get('descricao')
        data_final = request.POST.get('data_final')
        percentual_equity = request.POST.get('percentual_equity')
        estagio = request.POST.get('estagio')
        area = request.POST.get('area')
        publico_alvo = request.POST.get('publico_alvo')
        valor = request.POST.get('valor')
        pitch = request.FILES.get('pitch')
        logo = request.FILES.get('logo')

        try:
            empresa = Empresas(
                user=request.user,
                nome=nome,
                cnpj=cnpj,
                site=site,
                tempo_existencia=tempo_existencia,
                descricao=descricao,
                data_final_captacao=data_final,
                percentual_equity=percentual_equity,
                estagio=estagio,
                area=area,
                publico_alvo=publico_alvo,
                valor=valor,
                pitch=pitch,
                logo=logo
            )
            empresa.save()

        except ValidationError:
            messages.add_message(
                request,
                constants.ERROR,
                'Erro interno do servidor.'
            )
            return redirect('empresarios:cadastrar_empresa')

        messages.add_message(
            request,
            constants.SUCCESS,
            'Empresa cadastrada com sucesso.'
        )
        return redirect('empresarios:cadastrar_empresa')
