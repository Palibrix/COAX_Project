from django.shortcuts import render
from authentication.models import User


# Create your views here.
def hr(request):
    allData = User.objects.all()
    return render(request, 'hr/hr.html', locals())