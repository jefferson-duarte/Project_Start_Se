from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import redirect, render


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(
                request,
                constants.ERROR,
                'As senha nao coincidem.'
            )
            return redirect('usuarios:cadastro')

        if len(senha) < 6:
            messages.add_message(
                request,
                constants.ERROR,
                'A senha precisa ter pelomenos 6 digitos.'
            )
            return redirect('usuarios:cadastro')

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(
                request,
                constants.ERROR,
                'Usuario ja existe.'
            )
            return redirect('usuarios:cadastro')

        user = User.objects.create_user(
            username=username,
            password=senha
        )

    return redirect('cadastro:logar')


def logar(request):
    if request.method == 'GET':
        return render(request, 'logar.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('empresarios:cadastrar_empresa')

        messages.add_message(
            request,
            constants.ERROR,
            'Usuario ou senha invalidas.'
        )

        return redirect('usuarios:logar')
