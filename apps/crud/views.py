from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect


@login_required
def index(request):
    return render(request, "index.html")


@login_required
def novo_paciente(request):
    return render(request, "novo_paciente.html")


def sair(request):
    logout(request)
    return redirect('login')