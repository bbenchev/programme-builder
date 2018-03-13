from django.shortcuts import render
from .models import Module
from django.http import HttpResponse

def index(request):
    return render(request, "login.html", {})


def get_modules(request):
    context = {"modules": Module.objects.all()}


    return render(request, "modules.html", context)


def module(request,id):
    module = Module.objects.get(id=id)
    context = {"module": module}

    return render(request, "module.html", context)