from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

# from main.models import User
# from main.forms import MainForm

class MainPage(LoginView):
    # queryset = User.objects.order_by('id')
    template_name = 'main/index.html'
    # model = User
    # form_class = MainForm
    # return render(request, 'templates/main/index.html')

