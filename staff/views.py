from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import datetime
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from staff.models import Gang, Staff
from django.urls import reverse_lazy
# from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import ModuleRecievedForm, ModuleDefectForm
from django.db.models import Q
#from sidingz.models import ModuleRecieved
from staff.forms import GangForm, StaffForm


# Create your views here.


class StaffHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'staff/staff_home.html'


class GangListView(LoginRequiredMixin, ListView):
    model = Gang
    context_object_name = 'post'
    template_name = 'staff/gang_list.html'
    paginate_by = 20


class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    context_object_name = 'post'
    template_name = 'staff/staff_list.html'
    paginate_by = 20


class StaffEditView(LoginRequiredMixin, UpdateView):
    model = Staff
    fields = ['StaffName',
              'StaffMobileNumber', 'Designation',
              'StaffAddress',
              'DateOfJoining',
              ]
    template_name = 'staff/StaffList_edit.html'


class GangEditView(LoginRequiredMixin, UpdateView):
    model = Gang
    fields = ['GangName',
              'M1',
              'M2',
              'M3',
              'M4',
              'M5',
              'M6',
              'M7',
              'M8',
              'M9',
              'M10' ]
    template_name = 'staff/gangList_edit.html'


class StaffDetailView(LoginRequiredMixin, DetailView):
    model = Staff
    template_name = 'staff/staff_detail.html'


class GangDetailView(LoginRequiredMixin, DetailView):
    model = Gang
    template_name = 'staff/gang_detail.html'

@login_required
def AddStaff2(request):
    q = Staff.objects
    p = Gang.objects
    if request.method == 'POST':
        print(request.POST.get('StaffMobileNumber'))
        newStaff = Staff(
            StaffName=request.POST.get('StaffName'),
            Posted=request.POST.get('Posted1'),
            StaffMobileNumber=request.POST.get('StaffMobileNumber'),
            Designation=request.POST.get('Designation'),
            StaffAddress=request.POST.get('StaffAddress'),
            StaffToken=request.POST.get('StaffToken'),
            DateOfJoining=request.POST.get('DateOfJoining'),
            author=request.user)
        print(newStaff.Posted)
        newStaff.save()
        l = Staff.objects.all().order_by('-Date')
        message = messages.success(request, "Staff Added ")

        form6 = StaffForm()
        context = {
            'messages': message,
            'object_list': l,
            'form6': form6,
        }
        print('successful')
        return render(request, 'staff/staff_list2.html', context)

    else:
        message = messages.warning(request, "Staff Not Added ")
    form5 = StaffForm()
    form6 = StaffForm()
    l = Staff.objects.all().order_by('-Date')
    context = {
        'messages': message,
        'object_list': l,
        'form6': form6
    }
    return render(request, 'staff/staff_list2.html', context)



@login_required
def AddGang2(request):
    q = Staff.objects
    p = Gang.objects
    if request.method == 'POST':
        newGang = Gang(
            GangName=request.POST.get('GangName'),
            GPosted=request.POST.get('Posted2'),
            M1=q.filter(
                StaffName__iexact=request.POST.get('M1')).first(),
            M2=q.filter(
                StaffName__iexact=request.POST.get('M2')).first(),
            M3=q.filter(
                StaffName__iexact=request.POST.get('M3')).first(),
            M4=q.filter(
                StaffName__iexact=request.POST.get('M4')).first(),
            M5=q.filter(
                StaffName__iexact=request.POST.get('M5')).first(),
            M6=q.filter(
                StaffName__iexact=request.POST.get('M6')).first(),
            M7=q.filter(
                StaffName__iexact=request.POST.get('M7')).first(),
            M8=q.filter(
                StaffName__iexact=request.POST.get('M8')).first(),
            M9=q.filter(
                StaffName__iexact=request.POST.get('M9')).first(),
            M10=q.filter(
                StaffName__iexact=request.POST.get('M10')).first()
        )
        newGang.save()
        l = Gang.objects.all().order_by('-Date')
        message = messages.success(request, "Gang Added ")

        form6 = GangForm()
        context = {
            'messages': message,
            'object_list': l,
            'form6': form6,
        }
        print('successful')
        return render(request, 'staff/gang_list2.html', context)

    else:
        message = messages.warning(request, "Gang Not Added ")
    form5 = StaffForm()
    form6 = GangForm()
    l = Gang.objects.all().order_by('-Date')
    h = Gang.objects.all().first()
    print(h.GPosted)
    context = {
        'messages': message,
        'object_list': l,
        'form6': form6
    }
    return render(request, 'staff/gang_list2.html', context)


@login_required
def autocomplete1(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = Staff.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(StaffName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.StaffName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'staff/gang_entry_form.html')


@login_required
def staffName(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = Staff.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(StaffName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.StaffName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'staff/staff_list.html')


@login_required
def GangNumber(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = Gang.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(GangName__icontains=itemTerm)
            print("resGang")
            print(res)
            Item = list()
            for product in res:
                if product.GangName in Item:
                    pass
                else:
                    place_json = {}
                    place_json = product.GangName
                    Item.append(place_json)
                    print("*------JsonResponse Start-----*")
                    print(Item)
                    print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

    return render(request, 'sidings/ModulesList.html')


@login_required
def StaffDetailLink(request):
    if request.method == 'POST':
        StaffName = request.POST.get('staffName')
        print("StaffName")
        print(StaffName)
        qs = Staff.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(StaffName=StaffName)
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'staff/staff_list.html', context)


@login_required
def StaffDetailLink3(request):
    if request.method == 'POST':
        StaffName = request.POST.get('staffName')
        print("StaffName")
        print(StaffName)
        qs = Gang.objects
        print("qs")
        print(qs)
        res = qs.filter(Q(M1__StaffName__icontains=StaffName) |
                        Q(M2__StaffName__icontains=StaffName) |
                        Q(M3__StaffName__icontains=StaffName) |
                        Q(M4__StaffName__icontains=StaffName) |
                        Q(M5__StaffName__icontains=StaffName) |
                        Q(M6__StaffName__icontains=StaffName) |
                        Q(M7__StaffName__icontains=StaffName) |
                        Q(M8__StaffName__icontains=StaffName) |
                        Q(M9__StaffName__icontains=StaffName) |
                        Q(M10__StaffName__icontains=StaffName))
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
    context = {
        'object_list': res
    }
    return render(request, 'staff/gang_list.html', context)


@login_required
def GangDetailLink2(request):
    if request.method == 'POST':
        StaffName = request.POST.get('GangName')
        print("StaffName")
        print(StaffName)
        qs = Gang.objects
        print("qs")
        print(qs)
        res = qs.filter(GangName__icontains=StaffName)
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
    context = {
        'object_list': res
    }
    return render(request, 'staff/gang_list.html', context)


@login_required
def GangDetailLink3(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = Gang.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(GangName__icontains=itemTerm)
            print("resGang")
            print(res)
            Item = list()
            for product in res:
                if product.GangName in Item:
                    pass
                else:
                    place_json = {}
                    place_json = product.GangName
                    Item.append(place_json)
                    print("*------JsonResponse Start-----*")
                    print(Item)
                    print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

    return render(request, 'staff/StaffList.html')

