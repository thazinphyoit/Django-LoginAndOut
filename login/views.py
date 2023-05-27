from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

def login(request):
    pass

def register(request):
    if request.method == "POST" :
        print(1)
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    else :
        print(2)
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def logout(request):
    pass
