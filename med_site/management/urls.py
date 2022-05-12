from django.urls import path
from django.views.generic import TemplateView
from management import views

urlpatterns = [
    path('', views.hr, name='hr'),
    path('add/', TemplateView.as_view(template_name='hr/add.html'), name='add'),
    path('edit/', TemplateView.as_view(template_name='hr/edit.html'), name='edit'),
]
