from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from twilio.rest import Client
from django.conf import settings

# Create your models here.


class CCDDetails(models.Model):
    EXAMINATION_PLACE = (
        ("TKD_ACTL", "TKD ACTL"),
        ("TKD_HTPP_PWL", "TKD HTPP PWL"),
        ("TKD_ICD", "TKD ICD"),
        ("TKD_YARD", "TKD YARD"),
        )
    Serial = models.AutoField(primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    RakeName = models.CharField(max_length=50, null=True)
    ExamPlace = models.CharField(
        max_length=13, choices=EXAMINATION_PLACE, default='TKD YARD', null=True, blank=True)
    TKDInTime = models.DateTimeField(null=True)
    TKDOutTime = models.DateTimeField(null=True)
    YardInTime = models.DateTimeField(null=True)
    YardOutTime = models.DateTimeField(null=True)
    SidingIn = models.DateTimeField(null=True)
    SidingOut = models.DateTimeField(null=True)
    UnloadingStart = models.DateTimeField(null=True)
    UnloadingEnd = models.DateTimeField(null=True)
    LoadingStart = models.DateTimeField(null=True)
    LoadingEnd = models.DateTimeField(null=True)
    T431IssueTime = models.DateTimeField(null=True)
    T431ReceiveTime = models.DateTimeField(null=True)
    WorkStart = models.DateTimeField(null=True)
    WorkEnd = models.DateTimeField(null=True)
    BrakeBlock = models.IntegerField(null=True)
    Empad = models.IntegerField(null=True)
    AdopterChanged = models.IntegerField(null=True)
    AdopterCantt = models.IntegerField(null=True)
    SideBearerSpring = models.IntegerField(null=True)
    JawLinerWeld = models.IntegerField(null=True)
    ATLRepair = models.IntegerField(null=True)
    ROHDetachment = models.IntegerField(null=True)
    POHDetachment = models.IntegerField(null=True)
    DVSDetachment = models.IntegerField(null=True)
    TrafficDetention = models.TimeField(null=True)
    SidingDetention = models.TimeField(null=True)
    MechanicalDetention = models.TimeField(null=True)
    NewBPCNumber = models.BigIntegerField(null=True)
    NewBPCDate = models.DateField(null=True)
    OldBPCNumber = models.BigIntegerField(null=True)
    OldBPCDate = models.DateField(null=True)
