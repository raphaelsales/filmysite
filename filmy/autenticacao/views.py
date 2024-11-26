# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from .forms import RegistrationForm

class Login(View):
    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect('/')  # Redirect to the homepage if user is already authenticated
        else:
            return render(request, 'login.html', contexto)

    def post(self, request):
        # Obtém as credenciais de autenticação do formulário
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # Verifica as credenciais de autenticação fornecidas
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            # Verifica se o usuário ainda está ativo no sistema
            if user.is_active:
                login(request, user)
                return redirect('/')  # Redirect to the homepage upon successful login

            return render(request, 'login.html', {'mensagem': 'Usuário inativo.'})

        return render(request, 'login.html', {'mensagem': 'Usuário ou senha inválidos.'})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)

class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            form = RegistrationForm()
            return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/')
        return render(request, 'register.html', {'form': form})