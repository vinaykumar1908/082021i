from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import datetime
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rakes.models import Rake, Module
from django.urls import reverse_lazy
# from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import ModuleRecievedForm, ModuleDefectForm
from django.db.models import Q
from sidingz.models import ModuleRecieved
from rakes.forms import RakeForm, ModuleForm


# Create your views here.


class RakesHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'Rakes_home.html'


class RakeDetailView(LoginRequiredMixin, DetailView):
    model = Rake
    context_object_name = 'post'
    template_name = 'rakes/post_detail.html'


@login_required
def AddModule(request):
    form5 = ModuleForm()
    context = {
        'form5': form5,
    }
    if request.method == 'POST':
        print("******request.post1*******")
        print(request.POST)
        print(request.user)
        form = ModuleForm(request.POST)
        print(form)
       # form.author = request.user
        #print(form.author)
        if form.is_valid():
            print("form is true")
            M = form.cleaned_data['ModuleName']
            W1 = form.cleaned_data['Wagon1Number']
            W2 = form.cleaned_data['Wagon2Number']
            W3 = form.cleaned_data['Wagon3Number']
            W4 = form.cleaned_data['Wagon4Number']
            W5 = form.cleaned_data['Wagon5Number']

            added = Module(
                Date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ModuleName=M,
                Wagon1Number=W1, Wagon2Number=W2, Wagon3Number=W3, Wagon4Number=W4, Wagon5Number=W5)
            print(added)
            added.save()
            message = messages.success(request, "Module Added Successfully ")
        if not form.is_valid():
            message = messages.warning(request, "Module Not Added ")
            print("ERROR")
        form5 = ModuleForm()
        context = {
            'messages': message,
            'form5': form5,
        }

        return render(request, 'rakes/rake_entry_form.html', context)
        print('MPOST request accepted')
        pass
    print("MPOST Request bypassed")
    return render(request, 'rakes/rake_entry_form.html', context)


@login_required
def AddRake(request):
    form5 = ModuleForm()
    context = {
        'form5': form5,
    }
    if request.method == 'POST':
        form = RakeForm(request.POST)
        if form.is_valid():
            print("form is true")
            R = form.cleaned_data['RakeName']
            M1 = form.cleaned_data['Module1']
            M2 = form.cleaned_data['Module2']
            M3 = form.cleaned_data['Module3']
            M4 = form.cleaned_data['Module4']
            M5 = form.cleaned_data['Module5']
            M6 = form.cleaned_data['Module6']
            M7 = form.cleaned_data['Module7']
            M8 = form.cleaned_data['Module8']
            M9 = form.cleaned_data['Module9']
            #M4 = form.cleaned_data['Wagon4Number']
            #M5 = form.cleaned_data['Wagon5Number']
            added = Rake(
                Date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), RakeName=R,
                Module1=M1, Module2=M2, Module3=M3, Module4=M4, Module5=M5, Module6=M6, Module7=M7, Module8=M8, Module9=M9)
            print(added)
            added.save()
            message = messages.success(request, "Rake Added Successfully ")
            print(message)
        if not form.is_valid():
            message = messages.warning(request, "Rake Not Added ")
            print("ERROR")
            print(message)
        form5 = ModuleForm()
        context = {
            'messages': message,
            'form5': form5,
        }

        return render(request, 'rakes/rake_entry_form.html', context)
        print('RPOST request accepted')
        pass
    print("RPOST Request bypassed")
    return render(request, 'rakes/rake_entry_form.html', context)

@login_required
def autocomplete1(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = Module.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(ModuleName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.ModuleName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'rakes/rake_entry_form.html')


@login_required
def SidingModuleRecievedPageView(request):
    x = 1
    if request.method == 'POST':
        print(request.POST)
        form = ModuleRecievedForm(request.POST)
        if form.is_valid():
            RakeNumber0 = form.cleaned_data.get('RakeNumber', None)
            BPC_Number = form.cleaned_data.get('BPC_Number', None)

            ModulePresentPosition = form.cleaned_data.get(
                'ModulePresentPosition', None)

            ModuleName = form.cleaned_data.get('ModuleName', None)

            ModuleROHDate = form.cleaned_data.get('ModuleROHDate', None)

            ROHStation = form.cleaned_data.get('ROHStation', None)
            LineNumber = form.cleaned_data.get('LineNumber', None)

            Wagon1Number = form.cleaned_data.get('Wagon1Number', None)

            Wagon1Type = form.cleaned_data.get('Wagon1Type', None)
            Wagon2Number = form.cleaned_data.get('Wagon2Number', None)

            Wagon2Type = form.cleaned_data.get('Wagon2Type', None)
            Wagon3Number = form.cleaned_data.get('Wagon3Number', None)

            Wagon3Type = form.cleaned_data.get('Wagon3Type', None)
            Wagon4Number = form.cleaned_data.get('Wagon4Number', None)

            Wagon4Type = form.cleaned_data.get('Wagon4Type', None)
            Wagon5Number = form.cleaned_data.get('Wagon5Number', None)

            Wagon5Type = form.cleaned_data.get('Wagon5Type', None)
            Wagon1Defect = form.cleaned_data.get('Wagon1Defect', None)
            Wagon2Defect = form.cleaned_data.get('Wagon2Defect', None)
            Wagon3Defect = form.cleaned_data.get('Wagon3Defect', None)
            Wagon4Defect = form.cleaned_data.get('Wagon4Defect', None)
            Wagon5Defect = form.cleaned_data.get('Wagon5Defect', None)
            ModuleRecieveDate = form.cleaned_data.get(
                'ModuleRecieveDate', None)

            stockRecieved = form.cleaned_data.get('stockRecieved', None)
            ModuleDVS = form.cleaned_data.get('ModuleDVS', None)
            ModuleDVR = form.cleaned_data.get('ModuleDVR', None)
            ModuleMadeFit = form.cleaned_data.get('ModuleMadeFit', None)
            author = request.user
            print(Wagon1Defect)
            print(Wagon2Defect)
            print(Wagon3Defect)
            print(Wagon4Defect)
            print(Wagon5Defect)
            print(ModuleDVS)
            print(ModuleDVR)
            print(ModuleMadeFit)
            if ModuleDVS == True:
                MDVS = True
                print("MDVS")
                print(MDVS)
            else:
                MDVS = False
                print("MDVS")
                print(MDVS)

            if ModuleDVR == True:
                MDVR = True
                print("MDVR")
                print(MDVR)
            else:
                MDVR = False
                print("MDVR")
                print(MDVR)

            if ModuleMadeFit == True:
                MMF = True
                print("MMF")
                print(MMF)
            else:
                MMF = False
                print("MMF")
                print(MMF)
            added = models.ModuleRecieved.objects.create(
                RakeNumber=RakeNumber0, BPC_Number=BPC_Number,
                ModulePresentPosition=ModulePresentPosition,
                LineNumber=LineNumber, ModuleName=ModuleName,
                ModuleROHDate=ModuleROHDate, ROHStation=ROHStation, POHStation='POHStation',
                Wagon1Number=Wagon1Number, Wagon1Type=Wagon1Type,
                Wagon2Number=Wagon2Number, Wagon2Type=Wagon2Type,
                Wagon3Number=Wagon3Number, Wagon3Type=Wagon3Type,
                Wagon4Number=Wagon4Number, Wagon4Type=Wagon4Type,
                Wagon5Number=Wagon5Number, Wagon5Type=Wagon5Type,
                ModuleRecieveDate=ModuleRecieveDate, ModuleDVS=MDVS,
                ModuleDVR=MDVR, ModuleMadeFit=MMF, author=author, Wagon1Defect=Wagon1Defect, Wagon2Defect=Wagon2Defect, Wagon3Defect=Wagon3Defect, Wagon4Defect=Wagon4Defect, Wagon5Defect=Wagon5Defect)

            print(added.ModuleDVS)
            print(added.ModuleDVR)
            print(added.ModuleMadeFit)
            added.save()
            x = 1
            print("GO Through")
        else:
            print("did not GO THROUGH")
            x = 0
    form1 = ModuleRecievedForm()
    if x == 1:
        message = messages.success(request, "Success ")
    elif x == 0:
        message = messages.error(request, "Error ")
    context = {
        'messages': message,
        'form1': form1,
        'ModuleDefectForm': ModuleDefectForm()

    }

    return render(request, 'sidings/ModuleRecieved.html', context)
