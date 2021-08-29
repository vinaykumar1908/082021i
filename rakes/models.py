from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from twilio.rest import Client
from django.conf import settings




class Module(models.Model):
    WAGON_TYPE_CHOICES = (
        ("SelectWagon", "Please Select Wagon Type"),
        ("BLCA", "BLCA"),
        ("BLCB", "BLCB"),
        ("BLLA", "BLLA"),
        ("BLLB", "BLLB"),
        ("BLCMA", "BLCMA"),
        ("BLCMB", "BLCMB"),
        ("BVZC", "BVZC"),
        ("BVZI", "BVZI"),
        ("BFKHN", "BFKHN"),
    )
    Date = models.DateTimeField(default=timezone.now, null=True,blank=True)
    ModuleName = models.CharField(max_length=20, null=True, unique=True)
    Wagon1Number = models.BigIntegerField(null=True, blank=True)
    Wagon1Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon2Number = models.BigIntegerField(null=True, blank=True)
    Wagon2Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon3Number = models.BigIntegerField(null=True, blank=True)
    Wagon3Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon4Number = models.BigIntegerField(null=True, blank=True)
    Wagon4Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon5Number = models.BigIntegerField(null=True, blank=True)
    Wagon5Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    ModuleCommDate = models.DateField(
        null=True, default='1001-01-01', blank=True)
    ModuleROHDate = models.DateField(
        null=True, default='1001-01-01', blank=True)
    ModulePOHDate = models.DateField(
        null=True, default='1001-01-01', blank=True)
    Wagon1Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon2Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon3Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon4Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon5Defect = models.CharField(
        max_length=100, null=True, blank=True)
    ModuleDVS = models.BooleanField(default=False, blank=True)
    ModuleDVR = models.BooleanField(default=False, blank=True)
    ModuleDVSDate = models.DateField(null=True, blank=True)
    POHStation = models.CharField(max_length=100, null=True, blank=True)
    ROHStation = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='pid')

    def __str__(self):
        return str(self.ModuleName)

    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})

    


class Rake(models.Model):
    RAKE_BASE_LIST = (
        ("TKD_ACTL", "TKD ACTL"),
        ("TKD_HTPP_PWL", "TKD HTPP PWL"),
        ("TKD_ICD", "TKD ICD"),
        ("TKD_YARD", "TKD YARD"),
        ("SSB_ICD_GHH", "SSB ICD GHH"),
        ("SSB_ICD_PT", "SSB ICD PTT"),
        ("GZB_ICD_NOLI", "GZB ICD NOLI"),
        ("GZB_ICD_MUZ", "GZB ICD MUZ"),
        ("PNP_BMDJ", "PNP BMDJ"),
        ("PNP_PCWD_DWNA", "PNP PCWD DWNA"),
    )
    RakeName = models.CharField(max_length=100, unique=True, null=True)
    Date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    RakeBase = models.CharField(
        max_length=15, choices=RAKE_BASE_LIST, default='TKD_ICD', null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  blank=True, null=True, related_name='rid')
    Module1 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod1', blank=True, null=True)
    Module2 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod2', blank=True, null=True)
    Module3 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod3', blank=True, null=True)
    Module4 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod4', blank=True, null=True)
    Module5 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod5', blank=True, null=True)
    Module6 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod6', blank=True, null=True)
    Module7 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod7', blank=True, null=True)
    Module8 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod8', blank=True, null=True)
    Module9 = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='Mod9', blank=True, null=True)
        
    
    
    def __str__(self):
        return self.RakeName

    #def get_absolute_url(self):
        #return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        account_sid = "AC79222237cf68f0144f588d681e56907d"
        # Your Auth Token from twilio.com/console
        auth_token = "bee236c2075708556bd4e43049db5c05"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+919717631424",
            from_="+15393027840",
            body=f'Rake Name: {self.RakeName};')

        print(message.sid)
        print("Module Saved !")
        return super().save(*args, **kwargs)
