from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponse

import requests
# Create your views here.
class LoginView(View):
    template_name = 'login/login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/tesolimpiade/')

        form = LoginForm(request.POST or None)
        data = {
            'form': form
        }
        return render(request, self.template_name, data)


class AksiLoginView(View):
    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/tesolimpiade/')
            else:
                messages.add_message(request, messages.WARNING,
                                     'Username dan Password salah!!!')

        return redirect('/login/')


class AksiLogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/login/')



