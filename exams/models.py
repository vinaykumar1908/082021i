from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from twilio.rest import Client
from django.conf import settings
from rakes.models import Rake
from staff.models import Gang
# Create your models here.


class CCDetails(models.Model):
    EXAMINATION_PLACE = (
        ("TKD_ACTL", "TKD ACTL"),
        ("TKD_HTPP_PWL", "TKD HTPP PWL"),
        ("TKD_ICD", "TKD ICD"),
        ("TKD_YARD", "TKD YARD"),
        )
    Serial = models.AutoField(primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    RakeName = models.ForeignKey(
        Rake, on_delete=models.CASCADE, related_name='vcomments', default='1')
    Gang = models.ForeignKey(
        Gang, on_delete=models.CASCADE, related_name='v2comments', default='1')
    ExamPlace = models.CharField(
        max_length=13, choices=EXAMINATION_PLACE, default='TKD YARD', null=True, blank=True)
    TKDInTime = models.DateTimeField(null=True, blank=True)
    TKDOutTime = models.DateTimeField(null=True, blank=True)
    YardInTime = models.DateTimeField(null=True, blank=True)
    YardOutTime = models.DateTimeField(null=True, blank=True)
    SidingIn = models.DateTimeField(null=True, blank=True)
    SidingOut = models.DateTimeField(null=True, blank=True)
    UnloadingStart = models.DateTimeField(null=True, blank=True)
    UnloadingEnd = models.DateTimeField(null=True, blank=True)
    LoadingStart = models.DateTimeField(null=True, blank = True)
    LoadingEnd = models.DateTimeField(null=True, blank=True)
    T431IssueTime = models.DateTimeField(null=True, blank=True)
    T431ReceiveTime = models.DateTimeField(null=True, blank=True)
    WorkStart = models.DateTimeField(null=True, blank=True)
    WorkEnd = models.DateTimeField(null=True, blank=True)
    BrakeBlock = models.IntegerField(null=True, blank=True)
    Empad = models.IntegerField(null=True, blank=True)
    AdopterChanged = models.IntegerField(null=True, blank=True)
    AdopterCantt = models.IntegerField(null=True, blank=True)
    SideBearerSpring = models.IntegerField(null=True, blank=True)
    JawLinerWeld = models.IntegerField(null=True, blank=True)
    ATLRepair = models.IntegerField(null=True, blank=True)
    ROHDetachment = models.IntegerField(null=True, blank=True)
    POHDetachment = models.IntegerField(null=True, blank=True)
    DVSDetachment = models.IntegerField(null=True, blank=True)
    TrafficDetention = models.TimeField(null=True, blank=True)
    SidingDetention = models.TimeField(null=True, blank=True)
    MechanicalDetention = models.TimeField(null=True, blank=True)
    NewBPCNumber = models.BigIntegerField(null=True, blank=True)
    NewBPCDate = models.DateField(null=True, blank=True)
    OldBPCNumber = models.BigIntegerField(null=True, blank=True)
    OldBPCDate = models.DateField(null=True, blank=True)
    PreExamDetails = models.BooleanField(default='False', blank=True)
    ExamDetails = models.BooleanField(default='False', blank=True)
    PostExamDetails = models.BooleanField(default='False', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='ccid')
    examauthor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='examccid')
    postexamauthor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='postexamccid')
    def get_absolute_url(self):
        return reverse('Exams_home', kwargs={'pk': self.Serial})

    def get_queryset(self, *args, **kwargs):
        return CCDetails.objects.filter(Serial=self.args['pk'])

    def __str__(self):
        return str(self.RakeName)


class STRDetails(models.Model):
    EXAMINATION_PLACE = (
        ("TKD_ACTL", "TKD ACTL"),
        ("TKD_HTPP_PWL", "TKD HTPP PWL"),
        ("TKD_ICD", "TKD ICD"),
        ("TKD_YARD", "TKD YARD"),
    )
    Serial = models.AutoField(primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    RakeName = models.ForeignKey(
        Rake, on_delete=models.CASCADE, related_name='v1comments', default='1')
    Gang = models.ForeignKey(
        Gang, on_delete=models.CASCADE, related_name='v12comments', default='1')
    ExamPlace = models.CharField(
        max_length=13, choices=EXAMINATION_PLACE, default='TKD YARD', null=True, blank=True)
    TKDInTime = models.DateTimeField(null=True, blank=True)
    TKDOutTime = models.DateTimeField(null=True, blank=True)
    YardInTime = models.DateTimeField(null=True, blank=True)
    YardOutTime = models.DateTimeField(null=True, blank=True)
    SidingIn = models.DateTimeField(null=True, blank=True)
    SidingOut = models.DateTimeField(null=True, blank=True)
    UnloadingStart = models.DateTimeField(null=True, blank=True)
    UnloadingEnd = models.DateTimeField(null=True, blank=True)
    LoadingStart = models.DateTimeField(null=True, blank=True)
    LoadingEnd = models.DateTimeField(null=True, blank=True)
    T431IssueTime = models.DateTimeField(null=True, blank=True)
    T431ReceiveTime = models.DateTimeField(null=True, blank=True)
    WorkStart = models.DateTimeField(null=True, blank=True)
    WorkEnd = models.DateTimeField(null=True, blank=True)
    WorkReStart = models.DateTimeField(null=True, blank=True)
    WorkReEnd = models.DateTimeField(null=True, blank=True)
    BrakeBlock = models.IntegerField(null=True, blank=True)
    Empad = models.IntegerField(null=True, blank=True)
    AdopterChanged = models.IntegerField(null=True, blank=True)
    AdopterCantt = models.IntegerField(null=True, blank=True)
    SideBearerSpring = models.IntegerField(null=True, blank=True)
    JawLinerWeld = models.IntegerField(null=True, blank=True)
    ATLRepair = models.IntegerField(null=True, blank=True)
    ROHDetachment = models.IntegerField(null=True, blank=True)
    POHDetachment = models.IntegerField(null=True, blank=True)
    DVSDetachment = models.IntegerField(null=True, blank=True)
    TrafficDetention = models.TimeField(null=True, blank=True)
    SidingDetention = models.TimeField(null=True, blank=True)
    MechanicalDetention = models.TimeField(null=True, blank=True)
    NewBPCNumber = models.BigIntegerField(null=True, blank=True)
    NewBPCDate = models.DateField(null=True, blank=True)
    OldBPCNumber = models.BigIntegerField(null=True, blank=True)
    OldBPCDate = models.DateField(null=True, blank=True)
    PreExamDetails = models.BooleanField(default='False', blank=True)
    ExamDetails = models.BooleanField(default='False', blank=True)
    PostExamDetails = models.BooleanField(default='False', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='strid')
    examauthor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='examstrid')
    postexamauthor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='postexamstrid')

    def get_absolute_url(self):
        return reverse('Exams_home', kwargs={'pk': self.Serial})

    def get_queryset(self, *args, **kwargs):
        return CCDetails.objects.filter(Serial=self.args['pk'])

    def __str__(self):
        return str(self.RakeName)
