# Generated by Django 3.2.6 on 2021-08-28 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registerCurrentStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=100, unique=True)),
                ('PL_Number', models.BigIntegerField(unique=True)),
                ('AAC', models.IntegerField(default=0)),
                ('Stock', models.IntegerField()),
                ('updateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='registerStockDispatchedROH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=100)),
                ('PL_Number', models.IntegerField()),
                ('stockDispatched', models.IntegerField()),
                ('updateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='registerStockDispatchedSickline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=100)),
                ('PL_Number', models.IntegerField()),
                ('stockDispatched', models.IntegerField()),
                ('updateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='registerStockDispatchedTrainDuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=100)),
                ('PL_Number', models.IntegerField()),
                ('stockDispatched', models.IntegerField()),
                ('updateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='registerStockDispatchedYard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=100)),
                ('PL_Number', models.IntegerField()),
                ('stockDispatched', models.IntegerField()),
                ('Yard', models.CharField(choices=[('ACTL', 'ACTL'), ('HTPP', 'HTPP'), ('ICD_TKD', 'ICD_TKD'), ('ICD', 'ICD')], default='ACTL', max_length=7)),
                ('updateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='registerStockRecieved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=100)),
                ('AAC', models.IntegerField(default=0)),
                ('pl_Number', models.IntegerField()),
                ('stockRecieved', models.IntegerField()),
                ('stockRecievedChoices', models.CharField(choices=[('AMM', 'AMM'), ('JAGADHRI', 'JAGADHRI'), ('SHAKURBASTI', 'SHAKURBASTI')], default='AMM', max_length=11)),
                ('updateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
