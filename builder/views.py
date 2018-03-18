from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Module
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required



def login_handler(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "index.html", {"form": form})

@login_required(login_url="/")
def home(request):
    return render(request, "home.html", {})

def get_modules(request):
    context = {"modules": Module.objects.all()}
    return render(request, "modules.html", context)

def module(request,id):
    module = Module.objects.get(id=id)
    context = {"module": module}

    return render(request, "module.html", context)

@login_required(login_url="/")
def build(request):
    return render(request, "build.html", {})

def signup_handler(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})

def logout_handler(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")

