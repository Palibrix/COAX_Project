from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from django.conf import settings


class CustomLoginView(LoginView):
    template_name = 'authentication/authentication.html'

    def get_success_url(self):
        return reverse_lazy('mainPage')


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

