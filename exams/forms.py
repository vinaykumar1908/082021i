from django.forms import ModelForm
from rakes.models import Rake, Module
from .widgets import BootstrapDateTimePickerInput
from django import forms



class CCPostExForm(ModelForm):
    
    class Meta:
        model = Module
        fields = ['ModuleName', 'Wagon1Number', 'Wagon2Number',
                  'Wagon3Number', 'Wagon4Number', 'Wagon5Number']


class ModuleForm(ModelForm):

    class Meta:
        model = Module
        fields = ['ModuleName', 'Wagon1Number', 'Wagon2Number',
                  'Wagon3Number', 'Wagon4Number', 'Wagon5Number']
