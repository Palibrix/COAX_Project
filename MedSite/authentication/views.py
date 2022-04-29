from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.conf import settings
from django.contrib import messages


# ffR568Hkmmdl9
class CustomLoginView(LoginView):
    # def login_request(request):
    template_name = 'authentication/authentication.html'

    def get_success_url(self):
        return reverse_lazy('mainPage')

#     if request.method == "POST":
#         # print(request)
#         form = AuthenticationForm(request, data=request.POST)
#         print(form)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(username)
#             print(password)
#             user = authenticate(username=username, password=password)
#             print(1)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 print(2)
#                 return redirect("home")
#                 # return reverse_lazy('mainPage')
#             else:
#                 print(3)
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     print(4)
#     return render(request=request, template_name=template_name, context={"login_form": form})


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


def register_request(request):
    logout(request)
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register/register.html", context={"register_form": form})
