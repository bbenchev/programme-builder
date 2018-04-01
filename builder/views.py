from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, ProgrammeForm
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
    context = {}
    context["form"] = ProgrammeForm()
    context["modules1"] = Module.objects.filter(level="1")
    context["modules2"] = Module.objects.filter(level="2")
    context["modules3"] = Module.objects.filter(level="3")

    accreditations = Accreditation.objects.all()
    context["accreditations"] = accreditations
    for accreditation in accreditations:
        context[accreditation.abbreviation] = accreditation.criteria.all()

    print(context)
    return render(request, "build.html", context)

def signup_handler(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'form': form})

def logout_handler(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")

def get_criteria(request):
    index = request.get_full_path().index("?")
    parameter = request.get_full_path()[index+1:]
    accreditation = Accreditation.objects.filter(abbreviation=parameter)
    criteria = accreditation[0].criteria.all()
    context = {"criteria": []}
    for each in criteria:
        context["criteria"].append(each.definition)

    return JsonResponse(context)


def check_fulfilled(request, id):
    module = Module.objects.get(id=id)
    query_set = module.meets.all()
    fulfilled = {"criteria": []}
    for criterion in query_set:
        fulfilled["criteria"].append(criterion.definition)

    return JsonResponse(fulfilled)