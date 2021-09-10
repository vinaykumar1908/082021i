from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from stores import models as SM
#from sidingz import models as ZM
from django.urls import reverse_lazy
from django.db import models
import math
from datetime import date, datetime
from home import models as HM
from itertools import filterfalse
#from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rakes import models as RM


@login_required
class HomePageView(TemplateView):
    template_name = 'home.html'


@login_required
class SuccessPageView(TemplateView):
    template_name = 'success.html'


@login_required
def homeView(request):
    qs = RM.Module.objects.all()
        
        

    qs1 = RM.Rake.objects.all()

    j = timezone.now()

    #t = ZM.ModuleRecieved.objects.filter(ModuleRecieveDate__month=(j.month))
    #rs = t.filter(Q(ModuleDVS=True) & Q(ModuleMadeFit=False)).order_by("-ModuleRecieveDate")
    #rs1 = t.filter(Q(ModuleDVR=True) & Q(ModuleMadeFit=False)).order_by("-ModuleRecieveDate")
    
    #print('rs')
    #print(rs)
    #print('rs1')
    
    #print('rs2')
    
    #print()
    #qs2 = timezone.now()
    #a = ZM.ModuleRecieved.objects.filter(ModuleRecieveDate__month=(qs2.month))
    #prevDay = ZM.ModuleRecieved.objects.filter(ModuleRecieveDate__day=(qs2.day - 1))
    #Today = ZM.ModuleRecieved.objects.filter(ModuleRecieveDate__day=(qs2.day))
    #k = a.filter(Q(Wagon1Defect__icontains="em pad") | Q(Wagon1Defect__icontains="empad") | (Q(Wagon2Defect__icontains="em pad")) | Q(Wagon2Defect__icontains="empad") | (Q(Wagon3Defect__icontains="em pad")) | Q(Wagon3Defect__icontains="empad") | (Q(Wagon4Defect__icontains="em pad")) | Q(Wagon4Defect__icontains="empad") | (Q(Wagon5Defect__icontains="em pad") | Q(Wagon5Defect__icontains="empad"))).exclude(Q(ModulePresentPosition__icontains='TKD_ROH1') | Q(ModulePresentPosition__icontains='TKD_ROH2'))
    #l = a.filter(Q(Wagon1Defect__icontains="adopter") | (Q(Wagon2Defect__icontains="adopter")) | (Q(Wagon3Defect__icontains="adopter")) | (Q(Wagon4Defect__icontains="adopter")) | (Q(Wagon5Defect__icontains="adopter"))).filter(ModuleRecieveDate__month=(qs2.month))
    #m = a.filter(Q(ModuleMadeFit=True) & Q(ModuleDVR=True))
    #n = a.filter(Q(ModuleMadeFit=True) & Q(ModuleDVS=True))
    #o = a.filter(Q(ModuleDVR=True) & Q(ModuleRecieveDate__month=(qs2.month)))
    #print('k')
    #print(k)
    #print('k.count')
    #print(k.count())
    #print(l)

    context = {
        'obj': qs,
        'obj2': qs1,
        'time': j,
    }
    return render(request, 'home.html', context)
