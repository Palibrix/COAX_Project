from django.contrib.auth.views import LoginView
from django.shortcuts import render
from authentication.models import User

from django.urls import reverse_lazy
from django.views.generic import CreateView

# from mainPage.models import User
# from mainPage.forms import MainForm

class MainPage(LoginView):
    template_name = 'mainPage/mainPage.html'

    # def get_success_url(self):
    #     return reverse_lazy('login')

def SettingsPage(request):
    return render (request, 'settingsPage/settingsPage.html', locals())
