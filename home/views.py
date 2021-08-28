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


@login_required
class HomePageView(TemplateView):
    template_name = 'home.html'


@login_required
class SuccessPageView(TemplateView):
    template_name = 'success.html'


@login_required
def homeView(request):
    qs = SM.registerCurrentStock.objects.all()


    HM.p.objects.all().delete()
    qs1 = HM.p.objects.all()
    for l in qs:
        
        x = SM.registerCurrentStock.objects.get(id=l.id)
        
        y = HM.p.objects.create(id=x.id, Item=x.Item, AAC=x.AAC, Stock=x.Stock, updateTime=x.updateTime, PL_Number=x.PL_Number)
        y.MACfun()
        y.criticalFun()
        y.save()
        

    qs1 = HM.p.filterCriticalFun(request)
    qs1 = qs1.order_by('Stock')
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
        'obj': qs1,
        'obj2': qs1,
        'obj3': qs1,
        
        'obj4': qs1,
        'obj5': qs1,
        'obj6': qs1,
        'obj7': qs1,
        'obj8': qs1,
        'time': qs1,
        'objx': qs1,
        'objx1': qs1,


    }
    return render(request, 'home.html', context)
