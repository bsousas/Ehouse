from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from accounts.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

#Create your views here
def cadastro(request):
    template_name = 'usuarios/cadastro.html'
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect(settings.LOGIN_URL)

    return render(request, template_name, {'form': form})
