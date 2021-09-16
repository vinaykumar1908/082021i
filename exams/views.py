from django.shortcuts import render, get_object_or_404
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
from exams.models import CCDetails, STRDetails
from staff.models import Gang



# Create your views here.


class ExamHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'exams/CC_home.html'


class STRHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'exams/STR_home.html'



@login_required
def CCHomePageView(request):
    l = CCDetails.objects.all().order_by('-Date')
    context = {
        'object_list': l,
        #'form6': form6
    }
    return render(request, 'exams/CC_home.html', context)


@login_required
def STRHomePageView(request):
    l = STRDetails.objects.all().order_by('-Date')
    context = {
        'object_list': l,
        #'form6': form6
    }
    return render(request, 'exams/STR_home.html', context)



@login_required
def AddPreExamDetails(request):
    q = Module.objects
    p = Rake.objects
    if request.method == 'POST':
        newCC = CCDetails(
            RakeName=Rake.objects.get(RakeName=request.POST.get('RakeName')),
            ExamPlace=request.POST.get('ExamPlace'),
            TKDInTime=request.POST.get('TKDInTime'),
            OldBPCNumber=request.POST.get('OldBPCNumber'),
            YardInTime=request.POST.get('YardInTime'),
            SidingIn=request.POST.get('SidingIn'),
            UnloadingStart=request.POST.get('UnloadingStart'),
            T431IssueTime=request.POST.get('T431IssueTime'),
            T431ReceiveTime=request.POST.get('T431ReceiveTime'),
            author=request.user)
        newCC.PreExamDetails = True
        newCC.save()
        l = CCDetails.objects.all().order_by('-Date')
        message = messages.success(request, "CC Pre Exam Added ")
    
    #    form6 = ModuleForm()
    #    context = {
    #        'messages': message,
    #        'object_list': l,
    #        'form6': form6,
    #    }
    #    print('successful')
    #    return render(request, 'exams/CC_home.html', context)
    #
    #else:
    #    message = messages.warning(request, "Module Not Added ")
    #form5 = ModuleForm()
    #form6 = RakeForm()
    #c = self.pk
    #print(c)

        l = newCC
        print(l.Serial)
    #c = get_object_or_404(CCDetails, Serial = pk)
    #print(c)
 
    context = {
        #'messages': message,
        'object': l,
    }
    return render(request, 'exams/cc/ccpreexam.html', context)


@login_required
def AddExamDetails(request,Serial):
    q = CCDetails.objects.get(Serial=Serial)
    print(q)
    print(q.Date)
    print(q.ATLRepair)
    if request.method == 'POST':
        print("***********Start***********")
        
        q.examauthor=request.user
        q.ATLRepair=request.POST.get('ATLRepair')
        q.JawLinerWeld=request.POST.get('JawLinerWeld')
        q.SideBearerSpring=request.POST.get('SideBearerSpring')
        q.AdopterCantt=request.POST.get('AdopterCantt')
        q.AdopterChanged=request.POST.get('AdopterChanged')
        q.Empad=request.POST.get('Empad')
        q.BrakeBlock=request.POST.get('BrakeBlock')
        q.WorkEnd=request.POST.get('WorkEnd') 
        q.WorkStart=request.POST.get('WorkStart')
        q.ExamDetails = True
        print(q.ExamDetails)
        q.save()
        message = messages.success(request, "CC Exam Added ")
        l = CCDetails.objects.all().order_by('-Date')

    #    form6 = ModuleForm()
    #    context = {
    #        'messages': message,
    #        'object_list': l,
    #        'form6': form6,
    #    }
    #    print('successful')
    #    return render(request, 'exams/CC_home.html', context)
    #
    #else:
    #    message = messages.warning(request, "Module Not Added ")
    #form5 = ModuleForm()
    #form6 = RakeForm()
    #c = self.pk
    #print(c)

    p = q
    #c = get_object_or_404(CCDetails, Serial = pk)
    #print(c)

    context = {
        #'messages': message,
        'object': p,
    }
    return render(request, 'exams/cc/ccexam.html', context)


@login_required
def AddPostExamDetails(request, Serial):
    q = CCDetails.objects.get(Serial=Serial)
    print(q)
    print(q.Date)
    print(q.ATLRepair)
    if request.method == 'POST':
        print("***********Start***********")

        q.postexamauthor = request.user
        q.LoadingStart = request.POST.get('LoadingStart')
        q.LoadingEnd = request.POST.get('LoadingEnd')
        q.SidingOut = request.POST.get('SidingOut')
        q.YardOutTime = request.POST.get('YardOutTime')
        q.TKDOutTime = request.POST.get('TKDOutTime')
        q.ROHDetachment = request.POST.get('ROHDetachment')
        q.POHDetachment = request.POST.get('POHDetachment')
        q.DVSDetachment = request.POST.get('DVSDetachment')
        q.NewBPCNumber = request.POST.get('NewBPCNumber')
        q.NewBPCDate = request.POST.get('NewBPCDate')
        q.PostExamDetails = True
        print(q.ExamDetails)
        q.save()
        message = messages.success(request, "CC Post Exam Added ")
        l = CCDetails.objects.all().order_by('-Date')

    #    form6 = ModuleForm()
    #    context = {
    #        'messages': message,
    #        'object_list': l,
    #        'form6': form6,
    #    }
    #    print('successful')
    #    return render(request, 'exams/CC_home.html', context)
    #
    #else:
    #    message = messages.warning(request, "Module Not Added ")
    #form5 = ModuleForm()
    #form6 = RakeForm()
    #c = self.pk
    #print(c)

    p = q
    #c = get_object_or_404(CCDetails, Serial = pk)
    #print(c)

    context = {
        #'messages': message,
        'object': p,
    }
    return render(request, 'exams/cc/ccpostexam.html', context)


@login_required
def ShowCCExamDetails(request, Serial):
    q = CCDetails.objects.get(Serial=Serial)
    p = q
    #c = get_object_or_404(CCDetails, Serial = pk)
    #print(c)

    context = {
        #'messages': message,
        'object': p,
    }
    return render(request, 'exams/cc/ccdetails.html', context)


@login_required
def AddSTRPreExamDetails(request):
    q = Module.objects
    p = Rake.objects
    if request.method == 'POST':
        newCC = STRDetails(
            RakeName=Rake.objects.get(RakeName=request.POST.get('RakeName')),
            ExamPlace=request.POST.get('ExamPlace'),
            TKDInTime=request.POST.get('TKDInTime'),
            OldBPCNumber=request.POST.get('OldBPCNumber'),
            YardInTime=request.POST.get('YardInTime'),
            SidingIn=request.POST.get('SidingIn'),
            UnloadingStart=request.POST.get('UnloadingStart'),
            T431IssueTime=request.POST.get('T431IssueTime'),
            T431ReceiveTime=request.POST.get('T431ReceiveTime'),
            author=request.user)
        newCC.PreExamDetails = True
        newCC.save()
        l = STRDetails.objects.all().order_by('-Date')
        message = messages.success(request, "STR Pre Exam Added ")

    #    form6 = ModuleForm()
    #    context = {
    #        'messages': message,
    #        'object_list': l,
    #        'form6': form6,
    #    }
    #    print('successful')
    #    return render(request, 'exams/CC_home.html', context)
    #
    #else:
    #    message = messages.warning(request, "Module Not Added ")
    #form5 = ModuleForm()
    #form6 = RakeForm()
    #c = self.pk
    #print(c)

        l = newCC
        print(l.Serial)
    #c = get_object_or_404(CCDetails, Serial = pk)
    #print(c)

    context = {
        #'messages': message,
        'object': l,
    }
    return render(request, 'exams/str/strpreexam.html', context)


@login_required
def AddSTRExamDetails(request, Serial):
    q = STRDetails.objects.get(Serial=Serial)
    print(q)
    print(q.Date)
    print(q.ATLRepair)
    if request.method == 'POST':
        print("***********Start***********")

        q.examauthor = request.user
        q.ATLRepair = request.POST.get('ATLRepair')
        q.JawLinerWeld = request.POST.get('JawLinerWeld')
        q.SideBearerSpring = request.POST.get('SideBearerSpring')
        q.AdopterCantt = request.POST.get('AdopterCantt')
        q.AdopterChanged = request.POST.get('AdopterChanged')
        q.Empad = request.POST.get('Empad')
        q.BrakeBlock = request.POST.get('BrakeBlock')
        q.WorkEnd = request.POST.get('WorkEnd')
        q.WorkStart = request.POST.get('WorkStart')
        q.ExamDetails = True
        print(q.ExamDetails)
        q.save()
        message = messages.success(request, "STR Exam Added ")
        l = STRDetails.objects.all().order_by('-Date')

    #    form6 = ModuleForm()
    #    context = {
    #        'messages': message,
    #        'object_list': l,
    #        'form6': form6,
    #    }
    #    print('successful')
    #    return render(request, 'exams/CC_home.html', context)
    #
    #else:
    #    message = messages.warning(request, "Module Not Added ")
    #form5 = ModuleForm()
    #form6 = RakeForm()
    #c = self.pk
    #print(c)

    p = q
    #c = get_object_or_404(CCDetails, Serial = pk)
    #print(c)

    context = {
        #'messages': message,
        'object': p,
    }
    return render(request, 'exams/str/strexam.html', context)


@login_required
def AddSTRPostExamDetails(request, Serial):
    q = STRDetails.objects.get(Serial=Serial)
    print(q)
    print(q.Date)
    print(q.ATLRepair)
    if request.method == 'POST':
        print("***********Start***********")

        q.postexamauthor = request.user
        q.LoadingStart = request.POST.get('LoadingStart')
        q.LoadingEnd = request.POST.get('LoadingEnd')
        q.SidingOut = request.POST.get('SidingOut')
        q.YardOutTime = request.POST.get('YardOutTime')
        q.TKDOutTime = request.POST.get('TKDOutTime')
        q.ROHDetachment = request.POST.get('ROHDetachment')
        q.POHDetachment = request.POST.get('POHDetachment')
        q.DVSDetachment = request.POST.get('DVSDetachment')
        q.NewBPCNumber = request.POST.get('NewBPCNumber')
        q.NewBPCDate = request.POST.get('NewBPCDate')
        q.PostExamDetails = True
        print(q.ExamDetails)
        q.save()
        message = messages.success(request, "STR Post Exam Added ")
        l = STRDetails.objects.all().order_by('-Date')

    #    form6 = ModuleForm()
    #    context = {
    #        'messages': message,
    #        'object_list': l,
    #        'form6': form6,
    #    }
    #    print('successful')
    #    return render(request, 'exams/CC_home.html', context)
    #
    #else:
    #    message = messages.warning(request, "Module Not Added ")
    #form5 = ModuleForm()
    #form6 = RakeForm()
    #c = self.pk
    #print(c)

    p = q
    #c = get_object_or_404(CCDetails, Serial = pk)
    #print(c)

    context = {
        #'messages': message,
        'object': p,
    }
    return render(request, 'exams/str/strpostexam.html', context)


@login_required
def ShowSTRExamDetails(request, Serial):
    q = STRDetails.objects.get(Serial=Serial)
    p = q
    #c = get_object_or_404(CCDetails, Serial = pk)
    #print(c)

    context = {
        #'messages': message,
        'object': p,
    }
    return render(request, 'exams/str/strdetails.html', context)
