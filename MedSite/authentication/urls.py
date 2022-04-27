from django.urls import path

from authentication import views

urlpatterns = [
    path('authentication/', views.CustomLoginView.as_view(), name='authentication'),
    path('logout/', views.logout_request, name='logout'),

]
