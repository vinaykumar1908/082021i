from django.forms import ModelForm
from staff.models import Gang, Staff


class GangForm(ModelForm):

    class Meta:
        model = Gang
        fields = [
            'GangName','M1',
            'M2','M3',
             'M4', 'M5',
              'M6', 'M7',
               'M8', 'M9' ]


class StaffForm(ModelForm):

    class Meta:
        model = Staff
        fields = ['StaffName', 'StaffMobileNumber', 'Designation',
                  'StaffAddress', 'DateOfJoining']
