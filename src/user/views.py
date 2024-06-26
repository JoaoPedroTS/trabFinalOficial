from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Sua conta foi criada com sucesso {username}")
            return redirect("login")
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, "user/register.html", context)

@login_required
def profilePage(request):
    return render(request, "user/profile.html")