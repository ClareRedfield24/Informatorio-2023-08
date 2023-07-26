# from django.shortcuts import render
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.
class RegistrarUsuario(CreateView):
    template_name= "registration/registrar.html"
    form_class= RegistroUsuarioForm


    def form_valid(self, form):
        messages.success(self.request, "Registro exitoso. Por favor, inicia sesion")
        form.save()

        return redirect("apps.usuario:login")
    
class LoginUsuario(LoginView):
    template_name= "registration/login.html"

    def get_success_url(self):
        messages.success(self.request, "Inicio de Sesion Exitoso")
        return reverse("index")
    
class LogoutUsuario(LogoutView):
    template_name= "registration/logout.html"

    def get_success_url(self):
        messages.success(self.request, "Has cerrado Sesion")

        return reverse("apps.usuario:logout")