from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from twilio.rest import Client
from django.conf import settings


class Staff(models.Model):
    Designation = (
        ("Designation", "Please Select Designation"),
        ("Tech-3", "Tech-3"),
        ("Tech-2", "Tech-2"),
        ("Tech-1", "Tech-1"),
        ("Sr.Tech", "Sr.Tech"),
        ("MCM", "MCM"),
    )
    Posted = (
        ("TKD_ACTL", "TKD ACTL"),
        ("TKD_HTPP_PWL", "TKD HTPP PWL"),
        ("TKD_ICD", "TKD ICD"),
        ("TKD_YARD", "TKD YARD"),
        ("TKD_ROH1", "TKD ROH1"),
        ("TKD_ROH2", "TKD ROH2"),
        ("TKD_Sickline", "TKD Sickline"),
        ("TKD_Store", "TKD Store"),
        ("TKD_MnP", "TKD MnP"),
        ("TKD_TechCell", "TKD Tech Cell"),
    )
    Date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    Posted = models.CharField(
        max_length=30, choices=Posted, default='TKD_ROH1', null=True, blank=True)
    StaffName = models.CharField(max_length=50, null=True)
    StaffToken = models.CharField(max_length=4, null=True)
    StaffMobileNumber = models.BigIntegerField(null=True, blank=True)
    Designation = models.CharField(
        max_length=30, choices=Designation, default='Tech-3', null=True, blank=True)
    StaffAddress = models.CharField(max_length=150, null=True)
    DateOfJoining = models.DateField(null=True, blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='bid')

    def __str__(self):
        return str(self.StaffName)

    def get_absolute_url(self):
        return reverse('Staff_list')


class Gang(models.Model):
    Posted = (
        ("TKD_ACTL", "TKD ACTL"),
        ("TKD_HTPP_PWL", "TKD HTPP PWL"),
        ("TKD_ICD", "TKD ICD"),
        ("TKD_YARD", "TKD YARD"),
        ("TKD_ROH1", "TKD ROH1"),
        ("TKD_ROH2", "TKD ROH2"),
        ("TKD_Sickline", "TKD Sickline"),
        ("TKD_Store", "TKD Store"),
        ("TKD_MnP", "TKD MnP"),
        ("TKD_TechCell", "TKD Tech Cell"),
    )

    GangName = models.CharField(max_length=100, unique=True, default='Error')
    GPosted = models.CharField(
        max_length=30, choices=Posted, default='TKD_ROH1', null=True, blank=True)
    Date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    M1 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M1', blank=True, null=True)
    M2 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M2', blank=True, null=True)
    M3 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M3', blank=True, null=True)
    M4 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M4', blank=True, null=True)
    M5 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M5', blank=True, null=True)
    M6 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M6', blank=True, null=True)
    M7 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M7', blank=True, null=True)
    M8 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M8', blank=True, null=True)
    M9 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M9', blank=True, null=True)
    M10 = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='M10', blank=True, null=True)

    def __str__(self):
        return self.GangName

    def get_absolute_url(self):
        return reverse('Gangs_entry')

    #def save(self, *args, **kwargs):
    #    account_sid = "AC79222237cf68f0144f588d681e56907d"
        # Your Auth Token from twilio.com/console
    #    auth_token = "bee236c2075708556bd4e43049db5c05"

    #    client = Client(account_sid, auth_token)

    #    message = client.messages.create(
    #        to="+919717631424",
    #        from_="+15393027840",
    #        body=f'Rake Name: {self.RakeName};')

    #    print(message.sid)
    #    print("Module Saved !")
    #    return super().save(*args, **kwargs)
