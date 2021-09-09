from django.forms import ModelForm
from rakes.models import Rake, Module


class RakeForm(ModelForm):

    class Meta:
        model = Rake
        fields = ['RakeName', 'Module1', 'Module2',
                  'Module3', 'Module4', 'Module5', 'Module6', 'Module7', 'Module8', 'Module9', ]


class ModuleForm(ModelForm):

    class Meta:
        model = Module
        fields = ['ModuleName', 'Wagon1Number', 'Wagon2Number',
                  'Wagon3Number', 'Wagon4Number', 'Wagon5Number']



