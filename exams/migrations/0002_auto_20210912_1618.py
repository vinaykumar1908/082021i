# Generated by Django 3.2.6 on 2021-09-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccddetails',
            name='ExamDetails',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='ccddetails',
            name='PostExamDetails',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='ccddetails',
            name='PreExamDetails',
            field=models.BooleanField(default='False'),
        ),
    ]