# Generated by Django 3.2.6 on 2021-09-16 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20210911_1625'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rakes', '0007_alter_rake_rakename'),
        ('exams', '0009_auto_20210916_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccdetails',
            name='Gang',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='v2comments', to='staff.gang'),
        ),
        migrations.AlterField(
            model_name='ccdetails',
            name='RakeName',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='vcomments', to='rakes.rake'),
        ),
        migrations.CreateModel(
            name='STRDetails',
            fields=[
                ('Serial', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ExamPlace', models.CharField(blank=True, choices=[('TKD_ACTL', 'TKD ACTL'), ('TKD_HTPP_PWL', 'TKD HTPP PWL'), ('TKD_ICD', 'TKD ICD'), ('TKD_YARD', 'TKD YARD')], default='TKD YARD', max_length=13, null=True)),
                ('TKDInTime', models.DateTimeField(blank=True, null=True)),
                ('TKDOutTime', models.DateTimeField(blank=True, null=True)),
                ('YardInTime', models.DateTimeField(blank=True, null=True)),
                ('YardOutTime', models.DateTimeField(blank=True, null=True)),
                ('SidingIn', models.DateTimeField(blank=True, null=True)),
                ('SidingOut', models.DateTimeField(blank=True, null=True)),
                ('UnloadingStart', models.DateTimeField(blank=True, null=True)),
                ('UnloadingEnd', models.DateTimeField(blank=True, null=True)),
                ('LoadingStart', models.DateTimeField(blank=True, null=True)),
                ('LoadingEnd', models.DateTimeField(blank=True, null=True)),
                ('T431IssueTime', models.DateTimeField(blank=True, null=True)),
                ('T431ReceiveTime', models.DateTimeField(blank=True, null=True)),
                ('WorkStart', models.DateTimeField(blank=True, null=True)),
                ('WorkEnd', models.DateTimeField(blank=True, null=True)),
                ('WorkReStart', models.DateTimeField(blank=True, null=True)),
                ('WorkReEnd', models.DateTimeField(blank=True, null=True)),
                ('BrakeBlock', models.IntegerField(blank=True, null=True)),
                ('Empad', models.IntegerField(blank=True, null=True)),
                ('AdopterChanged', models.IntegerField(blank=True, null=True)),
                ('AdopterCantt', models.IntegerField(blank=True, null=True)),
                ('SideBearerSpring', models.IntegerField(blank=True, null=True)),
                ('JawLinerWeld', models.IntegerField(blank=True, null=True)),
                ('ATLRepair', models.IntegerField(blank=True, null=True)),
                ('ROHDetachment', models.IntegerField(blank=True, null=True)),
                ('POHDetachment', models.IntegerField(blank=True, null=True)),
                ('DVSDetachment', models.IntegerField(blank=True, null=True)),
                ('TrafficDetention', models.TimeField(blank=True, null=True)),
                ('SidingDetention', models.TimeField(blank=True, null=True)),
                ('MechanicalDetention', models.TimeField(blank=True, null=True)),
                ('NewBPCNumber', models.BigIntegerField(blank=True, null=True)),
                ('NewBPCDate', models.DateField(blank=True, null=True)),
                ('OldBPCNumber', models.BigIntegerField(blank=True, null=True)),
                ('OldBPCDate', models.DateField(blank=True, null=True)),
                ('PreExamDetails', models.BooleanField(blank=True, default='False')),
                ('ExamDetails', models.BooleanField(blank=True, default='False')),
                ('PostExamDetails', models.BooleanField(blank=True, default='False')),
                ('Gang', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='v12comments', to='staff.gang')),
                ('RakeName', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='v1comments', to='rakes.rake')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strid', to=settings.AUTH_USER_MODEL)),
                ('examauthor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examstrid', to=settings.AUTH_USER_MODEL)),
                ('postexamauthor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postexamstrid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
