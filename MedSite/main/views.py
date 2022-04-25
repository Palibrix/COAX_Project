from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from main.models import User
# from main.forms import MainForm

class MainPage(LoginView):
    template_name = 'main/mainPage.html'

    # def get_success_url(self):
    #     return reverse_lazy('login')

