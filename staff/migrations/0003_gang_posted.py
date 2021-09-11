# Generated by Django 3.2.6 on 2021-09-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staff_stafftoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='gang',
            name='Posted',
            field=models.CharField(blank=True, choices=[('TKD_ACTL', 'TKD ACTL'), ('TKD_HTPP_PWL', 'TKD HTPP PWL'), ('TKD_ICD', 'TKD ICD'), ('TKD_YARD', 'TKD YARD'), ('TKD_ROH1', 'TKD ROH1'), ('TKD_ROH2', 'TKD ROH2'), ('TKD_Sickline', 'TKD Sickline'), ('TKD_Store', 'TKD Store'), ('TKD_MnP', 'TKD MnP'), ('TKD_TechCell', 'TKD Tech Cell')], default='TKD_ROH1', max_length=30, null=True),
        ),
    ]
