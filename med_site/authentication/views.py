from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from core import settings


class CustomLoginView(LoginView):
    template_name = 'login/login.html'

    def get_success_url(self):
        return reverse_lazy('')


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

# Now it is not working, but I'm a little tired, so i go to sleep to continue on the next day

def register_request(request):

    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.clened_data['username']
    #         password = form.clened_data['password1']
    #         user = auth(username=username, password = password)
    #         login(request, user)
    #         massage.succes(request, ("Registration are Successful"))
    #         return redirect('home')
    # else:
    #     form = UserCreationForm()

    return render(request, 'register/register.html', {
       # 'form':form,
    })


