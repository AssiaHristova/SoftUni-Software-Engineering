from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from core.decorators import any_group_required
from .forms import PythonCreateForm
from .models import Python


def sign_in(request):
    user = authenticate(username='raya', password='Muncheto')
    login(request, user)
    return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


@login_required(login_url=reverse_lazy('sign-in'))
@any_group_required(groups=['User'])
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(req, 'create.html', {'form': form})
