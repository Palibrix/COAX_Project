from django.urls import path
from mainPage import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='mainPage'),
    path('settings', views.SettingsPage, name='settings'),
    path('staff', views.Stuff, name='staff'),
    path('addDoctor', views.AddDoc, name='addDoctor'),
]