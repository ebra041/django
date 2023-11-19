from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here.


def register_get(request):
    form = UserForm()
    if request.method == 'GET':
        form = UserForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/postget/regget/')
    context = {'form':form}
    return render(request, 'registerget.html',context)

def register_post(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/postget/regpost/')
    context = {'form':form}
    return render(request, 'registerpost.html',context)