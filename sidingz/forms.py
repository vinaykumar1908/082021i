from django.forms import ModelForm
from .models import ModuleRecieved


class ModuleRecievedForm(ModelForm):

    class Meta:
        model = ModuleRecieved
        fields = ('RakeNumber', 'BPC_Number',
                  'ModulePresentPosition',
                  'LineNumber', 'ModuleName',
                  'ModuleROHDate', 'ROHStation', 'POHStation',
                  'Wagon1Number', 'Wagon2Number', 'Wagon3Number', 'Wagon4Number', 'Wagon5Number',
                  'Wagon1Type',
                  'Wagon2Type', 'Wagon3Type',
                  'Wagon4Type',
                  'Wagon5Type',
                  'Wagon1Defect',
                  'Wagon2Defect',
                  'Wagon3Defect',
                  'Wagon4Defect',
                  'Wagon5Defect',
                  'ModuleRecieveDate', 'ModuleDVS',
                  'ModuleDVR', 'ModuleMadeFit')

class ModuleDefectForm(ModelForm):
    
    class Meta:
        model = ModuleRecieved
        fields = ('Wagon1Type',
                  'Wagon2Type', 'Wagon3Type',
                  'Wagon4Type',
                  'Wagon5Type',
        )
