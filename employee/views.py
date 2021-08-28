from django.shortcuts import render
#from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def home(request):
    x = User.objects.all()
    print(x.first())
    x = x.order_by('id')
    context = {
        'x': x,
    }

    return render(request, 'emp/home.html', context)

class detail(DetailView):
    model = User
    template_name = 'emp/profile.html'
