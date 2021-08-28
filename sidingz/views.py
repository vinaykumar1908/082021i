from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sidingz import models
from django.urls import reverse_lazy
# from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ModuleRecievedForm, ModuleDefectForm
from django.db.models import Q

# Create your views here.


class SidingHomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'sidings_home.html'


class SidingICDOkhlaHomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'sidings/ICD_Okhla_home.html'


@login_required
def SidingModuleRecievedPageView(request):
    x = 1
    if request.method == 'POST':
        print(request.POST)
        form = ModuleRecievedForm(request.POST)
        if form.is_valid():
            RakeNumber0 = form.cleaned_data.get('RakeNumber', None)
            BPC_Number = form.cleaned_data.get('BPC_Number', None)

            ModulePresentPosition = form.cleaned_data.get('ModulePresentPosition', None)

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
            ModuleRecieveDate = form.cleaned_data.get('ModuleRecieveDate', None)

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


class SidingModuleListPageView(LoginRequiredMixin, ListView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList.html'
    ordering = ['-Date']
    paginate_by = 50


class SidingModuleDetailPageView(LoginRequiredMixin, DetailView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList_detail.html'


class SidingModuleEditView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['RakeNumber', 'BPC_Number',
              'LineNumber', 'ModuleName', 
              'ROHStation', 'POHStation',
              'Wagon1Number', 'Wagon1Type',
              'Wagon2Number', 'Wagon2Type',
              'Wagon3Number', 'Wagon3Type',
              'Wagon4Number', 'Wagon4Type',
              'Wagon5Number', 'Wagon5Type',
              'ModuleRecieveDate']
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditROHDateView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['ModuleROHDate', 'ModulePOHDate']
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditDefectView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['Wagon1Defect', 'Wagon2Defect',
              'Wagon3Defect', 'Wagon4Defect', 'Wagon5Defect', ]
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditDVSView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['ModuleDVS', 'ModuleDVR',  'ModuleDVSDate',
              'ModulePresentPosition', 'ModuleMadeFit',
              'ModuleMadeFitDateTime']
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditROHFileView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['ROHFile']
    template_name = 'sidings/ModulesList_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SidingModuleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList_delete.html'
    success_url = reverse_lazy('siding_Modules_List')


@login_required
def moduleName(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = models.ModuleRecieved.objects.all()
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
            
    return render(request, 'sidings/ModulesList.html')


@login_required
def RakeNumber(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = models.ModuleRecieved.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(RakeNumber__icontains=itemTerm)
            print("resRAKE")
            print(res)
            Item = list()
            for product in res:
                if product.RakeNumber in Item:
                    pass
                else:
                    place_json = {}
                    place_json = product.RakeNumber
                    Item.append(place_json)
                    print("*------JsonResponse Start-----*")
                    print(Item)
                    print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

    return render(request, 'sidings/ModulesList.html')


@login_required
def WagonNumber(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = models.ModuleRecieved.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Q(Wagon1Number__icontains=itemTerm) | Q(Wagon2Number__icontains=itemTerm) | Q(Wagon3Number__icontains=itemTerm) | Q(Wagon4Number__icontains=itemTerm) | Q(Wagon5Number__icontains=itemTerm))
            print("resRAKE")
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

    return render(request, 'sidings/ModulesList.html')

@login_required
def ModuleDetailLink(request):
    if request.method=='POST':
        ModuleName = request.POST.get('moduleName')
        print("ModuleName")
        print(ModuleName)
        qs = models.ModuleRecieved.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(ModuleName=ModuleName)
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list' : res
        }
    return render(request, 'sidings/ModulesList.html', context)


@login_required
def RakeDetailLink(request):
    if request.method == 'POST':
        RakeNumber = request.POST.get('RakeNumber')
        print("RakeNumber")
        print(RakeNumber)
        qs = models.ModuleRecieved.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(RakeNumber=RakeNumber)
        res = res.order_by("-ModuleROHDate")
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesList.html', context)
        

@login_required
def WagonDetailLink(request):
    if request.method == 'POST':
        WagonNumber = request.POST.get('WagonNumber')
        print("WagonNumber")
        print(WagonNumber)
        qs = models.ModuleRecieved.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(ModuleName__icontains=WagonNumber)
        res = res.order_by("-ModuleRecieveDate")
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesList.html', context)

@login_required
def DateDetailLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        print("date1")
        print(date1)
        print("date2")
        print(date2)
        qs = models.ModuleRecieved.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(ModuleRecieveDate__range=[date1, date2])
        res = res.order_by("-ModuleROHDate")
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesList.html', context)


@login_required
def DateDetailGZBMUZLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='GZB_ICD_MUZ')
        res = res.order_by("-ModuleRecieveDate")
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListGZBMUZ.html', context)


@login_required
def DateDetailGZBNOLILink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='GZB_ICD_NOLI')
        res = res.order_by("-ModuleRecieveDate")
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListGZBNOLI.html', context)


@login_required
def DateDetailPNPBMDJLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='PNP_BMDJ')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListPNPBMDJ.html', context)


@login_required
def DateDetailPNPDWNALink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='PNP_PCWD_DWNA')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListPNPDWNA.html', context)


@login_required
def DateDetailSSBGHHLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='SSB_ICD_GHH')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListSSBGHH.html', context)


@login_required
def DateDetailSSBPTTLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='SSB_ICD_PT')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListSSBPTT.html', context)


@login_required
def DateDetailTKDACTLLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='TKD_ACTL')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListTKDACTL.html', context)


@login_required
def DateDetailTKDHTPPLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='TKD_HTPP_PWL')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListTKDHTPP.html', context)


@login_required
def DateDetailTKDICDLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[
                        date1, date2], ModulePresentPosition__icontains='TKD_ICD')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListTKDICD.html', context)


@login_required
def DateDetailYardLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='TKD_YARD')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListYard.html', context)


@login_required
def TKDICDModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_ICD")
    res1 = res.filter(ModuleDVS=True).order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDICD.html', context)


@login_required
def TKDICDModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_ICD")
    res = res.filter(ModuleDVS=True).order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDICD.html', context)


@login_required
def TKDHTPPModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_HTPP_PWL").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDHTPP.html', context)


@login_required
def TKDHTPPModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_HTPP_PWL").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDHTPP.html', context)


@login_required
def TKDACTLModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_ACTL").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDACTL.html', context)


@login_required
def TKDACTLModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_ACTL").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDACTL.html', context)


@login_required
def SSBGHHModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="SSB_ICD_GHH").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListSSBGHH.html', context)


@login_required
def SSBGHHModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="SSB_ICD_GHH").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListSSBGHH.html', context)


@login_required
def SSBPTTModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="SSB_ICD_PT").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListSSBGHH.html', context)


@login_required
def SSBPTTModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="SSB_ICD_PT").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListSSBPTT.html', context)


@login_required
def PNPBMDJModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="PNP_BMDJ").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListPNPBMDJ.html', context)


@login_required
def PNPBMDJModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="PNP_BMDJ").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListPNPBMDJ.html', context)


@login_required
def PNPDWNAModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="PNP_PCWD_DWNA").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListPNPDWNA.html', context)


@login_required
def PNPDWNAModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="PNP_PCWD_DWNA")
    res = res.filter(ModuleDVS=True).order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListPNPDWNA.html', context)


@login_required
def GZBNOLIModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="GZB_ICD_NOLI").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListGZBNOLI.html', context)


@login_required
def GZBNOLIModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="GZB_ICD_NOLI").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListGZBNOLI.html', context)


@login_required
def GZBMUZModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="GZB_ICD_MUZ").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListGZBMUZ.html', context)


@login_required
def GZBMUZModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="GZB_ICD_MUZ")
    res = res.filter(ModuleDVS=True).order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListGZBMUZ.html', context)


@login_required
def YardModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_YARD").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListYard.html', context)
