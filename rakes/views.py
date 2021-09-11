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


class RakeListView(LoginRequiredMixin, ListView):
    model = Rake
    context_object_name = 'post'
    template_name = 'rakes/rake_list.html'
    ordering = ['-Date']
    paginate_by = 20


class ModuleListView(LoginRequiredMixin, ListView):
    model = Module
    context_object_name = 'post'
    template_name = 'rakes/module_list.html'
    paginate_by = 20


class ModuleEditView(LoginRequiredMixin, UpdateView):
    model = Module
    fields = ['ModuleName',
              'ROHStation', 'POHStation',
              'Wagon1Number',
              'Wagon2Number',
              'Wagon3Number',
              'Wagon4Number',
              'Wagon5Number', 'ModuleType', 'ModuleCommDate', 'ModuleROHDate', 'ModulePOHDate', 'Modified']
    template_name = 'rakes/ModulesList_edit.html'


class RakeEditView(LoginRequiredMixin, UpdateView):
    model = Rake
    fields = ['RakeName',
              'RakeBase', 
              'Module1',
              'Module2', 
              'Module3', 
              'Module4', 
              'Module5', 
              'Module6', 
              'Module7', 
              'Module8', 
              'Module9']
    template_name = 'rakes/rakeList_edit.html'
class ModuleDetailView(LoginRequiredMixin, DetailView):
    model = Module
    template_name = 'rakes/module_detail.html'

class RakeDetailView(LoginRequiredMixin, DetailView):
    model = Rake
    template_name = 'rakes/rake_detail.html'

@login_required
def AddModule(request):
    q = Module.objects
    p = Rake.objects
    if request.method == 'POST':
        newModule = Module(
            ModuleName=request.POST.get('ModuleName'),
            Wagon1Number=request.POST.get('W1'),
            Wagon2Number=request.POST.get('W2'),
            Wagon3Number=request.POST.get('W3'),
            Wagon4Number=request.POST.get('W4'),
            Wagon5Number=request.POST.get('W5'),
            ModuleROHDate=request.POST.get('ROHDate'),
            ModulePOHDate=request.POST.get('POHDate'),
            ModuleType=request.POST.get('ModuleType'),
            Modified=request.POST.get('fav_language'),
            author=request.user)
        newModule.save()
        l = Module.objects.all().order_by('-Date')
        message = messages.success(request, "Module Added ")

        form6 = ModuleForm()
        context = {
            'messages': message,
            'object_list': l,
            'form6': form6,
        }
        print('successful')
        return render(request, 'rakes/module_list.html', context)

    else:
        message = messages.warning(request, "Module Not Added ")
    form5 = ModuleForm()
    form6 = RakeForm()
    l = Module.objects.all().order_by('-Date')
    context = {
        'messages': message,
        'object_list': l,
        'form6': form6
    }
    return render(request, 'rakes/module_list.html', context)

@login_required
def AddRake(request):
    q = Module.objects
    p = Rake.objects
    if request.method == 'POST':
        newRake = Rake(
            RakeName=request.POST.get('RakeName'),
            Module1=q.filter(
                ModuleName__iexact=request.POST.get('M1')).first(),
            Module2=q.filter(
                ModuleName__iexact=request.POST.get('M2')).first(),
            Module3=q.filter(
                ModuleName__iexact=request.POST.get('M3')).first(),
            Module4=q.filter(
                ModuleName__iexact=request.POST.get('M4')).first(),
            Module5=q.filter(
                ModuleName__iexact=request.POST.get('M5')).first(),
            Module6=q.filter(
                ModuleName__iexact=request.POST.get('M6')).first(),
            Module7=q.filter(
                ModuleName__iexact=request.POST.get('M7')).first(),
            Module8=q.filter(
                ModuleName__iexact=request.POST.get('M8')).first(),
            Module9=q.filter(
                ModuleName__iexact=request.POST.get('M9')).first(),
            RakeBase=request.POST.get('Base'), author=request.user)
        newRake.save()
        l = Rake.objects.all().order_by('-Date')
        message = messages.success(request, "Rake Added ")

        form6 = RakeForm()
        context = {
            'messages': message,
            'object_list': l,
            'form6': form6,
        }
        print('successful')
        return render(request, 'rakes/rake_list.html', context)

    else:
        message = messages.warning(request, "Rake Not Added ")
    form5 = ModuleForm()
    form6 = RakeForm()
    l = Rake.objects.all().order_by('-Date')
    context = {
        'messages': message,
        'object_list': l,
        'form6': form6
    }
    return render(request, 'rakes/rake_list.html', context)
    



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
def moduleName(request):
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

            return render(request, 'rakes/module_list.html')
@login_required
def RakeNumber(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = Rake.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(__icontains=itemTerm)
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
def ModuleDetailLink(request):
    if request.method == 'POST':
        ModuleName = request.POST.get('moduleName')
        print("ModuleName")
        print(ModuleName)
        qs = Module.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(ModuleName=ModuleName)
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'rakes/module_list.html', context)


@login_required
def ModuleDetailLink3(request):
    if request.method == 'POST':
        ModuleName = request.POST.get('moduleName')
        print("ModuleName")
        print(ModuleName)
        qs = Rake.objects
        print("qs")
        print(qs)
        res = qs.filter(Q(Module1__ModuleName__icontains=ModuleName) |
                     Q(Module2__ModuleName__icontains=ModuleName) |
                     Q(Module3__ModuleName__icontains=ModuleName) |
                     Q(Module4__ModuleName__icontains=ModuleName) |
                     Q(Module5__ModuleName__icontains=ModuleName) |
                     Q(Module6__ModuleName__icontains=ModuleName) |
                     Q(Module7__ModuleName__icontains=ModuleName) |
                     Q(Module8__ModuleName__icontains=ModuleName) |
                     Q(Module9__ModuleName__icontains=ModuleName) )
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
    context = {
        'object_list': res
    }
    return render(request, 'rakes/rake_list.html', context)


@login_required
def RakeDetailLink2(request):
    if request.method == 'POST':
        ModuleName = request.POST.get('RakeNumber')
        print("ModuleName")
        print(ModuleName)
        qs = Rake.objects
        print("qs")
        print(qs)
        res = qs.filter(RakeName__icontains=ModuleName)
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
    context = {
        'object_list': res
    }
    return render(request, 'rakes/rake_list.html', context)


@login_required
def RakeDetailLink3(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = Rake.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(RakeName__icontains=itemTerm)
            print("resRAKE")
            print(res)
            Item = list()
            for product in res:
                if product.RakeName in Item:
                    pass
                else:
                    place_json = {}
                    place_json = product.RakeName
                    Item.append(place_json)
                    print("*------JsonResponse Start-----*")
                    print(Item)
                    print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

    return render(request, 'sidings/ModulesList.html')


@login_required
def wagonnumberlink(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = Module.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Q(Wagon1Number__icontains=itemTerm) |
                            Q(Wagon2Number__icontains=itemTerm) |
                            Q(Wagon3Number__icontains=itemTerm) |
                            Q(Wagon4Number__icontains=itemTerm) |
                            Q(Wagon5Number__icontains=itemTerm) )
            print("resRAKE")
            print(res)
            Item = list()
            for product in res:
                if product.ModuleName in Item:
                    pass
                else:
                    place_json = {}
                    place_json = product.ModuleName
                    Item.append(place_json)
                    print("*------JsonResponse Start-----*")
                    print(Item)
                    print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

    return render(request, 'sidings/ModulesList.html')


@login_required
def WagonDetailLink(request):
    if request.method == 'POST':
        ModuleName = request.POST.get('wagonnumber')
        print("ModuleName")
        print(ModuleName)
        qs = Module.objects
        print("qs")
        print(qs)
        res = qs.filter(ModuleName__icontains=ModuleName)
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
    context = {
        'object_list': res
    }
    return render(request, 'rakes/module_list.html', context)
