from django.urls import path

from COAX_Project.med_site.authentication import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_request, name='logout'),
    # path('register/', views.register_request, name='register')
]