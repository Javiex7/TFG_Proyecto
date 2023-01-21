from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def signup(request):
    if (request.method == "POST"):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request=request, user=user)

            return redirect('/')
