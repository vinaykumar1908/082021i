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


class ExamHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'exams/Exam_home.html'


class CCHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'exams/CC_home.html'


class STRHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'exams/STR_home.html'
