from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_message = "Welcome, you are successfully logged in!"
