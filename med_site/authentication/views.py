from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from COAX_Project.med_site.core import settings


class CustomLoginView(LoginView):
    template_name = 'login/login.html'

    def get_success_url(self):
        return reverse_lazy('')


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


