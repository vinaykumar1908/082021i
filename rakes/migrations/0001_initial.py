# Generated by Django 3.2.6 on 2021-08-29 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('ModuleName', models.CharField(max_length=20, null=True, unique=True)),
                ('Wagon1Number', models.BigIntegerField(blank=True, null=True)),
                ('Wagon1Type', models.CharField(blank=True, choices=[('SelectWagon', 'Please Select Wagon Type'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BLCMA', 'BLCMA'), ('BLCMB', 'BLCMB'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True)),
                ('Wagon2Number', models.BigIntegerField(blank=True, null=True)),
                ('Wagon2Type', models.CharField(blank=True, choices=[('SelectWagon', 'Please Select Wagon Type'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BLCMA', 'BLCMA'), ('BLCMB', 'BLCMB'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True)),
                ('Wagon3Number', models.BigIntegerField(blank=True, null=True)),
                ('Wagon3Type', models.CharField(blank=True, choices=[('SelectWagon', 'Please Select Wagon Type'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BLCMA', 'BLCMA'), ('BLCMB', 'BLCMB'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True)),
                ('Wagon4Number', models.BigIntegerField(blank=True, null=True)),
                ('Wagon4Type', models.CharField(blank=True, choices=[('SelectWagon', 'Please Select Wagon Type'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BLCMA', 'BLCMA'), ('BLCMB', 'BLCMB'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True)),
                ('Wagon5Number', models.BigIntegerField(blank=True, null=True)),
                ('Wagon5Type', models.CharField(blank=True, choices=[('SelectWagon', 'Please Select Wagon Type'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BLCMA', 'BLCMA'), ('BLCMB', 'BLCMB'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True)),
                ('ModuleCommDate', models.DateField(blank=True, default='1001-01-01', null=True)),
                ('ModuleROHDate', models.DateField(blank=True, default='1001-01-01', null=True)),
                ('ModulePOHDate', models.DateField(blank=True, default='1001-01-01', null=True)),
                ('Wagon1Defect', models.CharField(blank=True, max_length=100, null=True)),
                ('Wagon2Defect', models.CharField(blank=True, max_length=100, null=True)),
                ('Wagon3Defect', models.CharField(blank=True, max_length=100, null=True)),
                ('Wagon4Defect', models.CharField(blank=True, max_length=100, null=True)),
                ('Wagon5Defect', models.CharField(blank=True, max_length=100, null=True)),
                ('ModuleDVS', models.BooleanField(blank=True, default=False)),
                ('ModuleDVR', models.BooleanField(blank=True, default=False)),
                ('ModuleDVSDate', models.DateField(blank=True, null=True)),
                ('POHStation', models.CharField(blank=True, max_length=100, null=True)),
                ('ROHStation', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RakeName', models.CharField(max_length=100, unique=True)),
                ('Date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('RakeBase', models.CharField(blank=True, choices=[('TKD_ACTL', 'TKD ACTL'), ('TKD_HTPP_PWL', 'TKD HTPP PWL'), ('TKD_ICD', 'TKD ICD'), ('TKD_YARD', 'TKD YARD'), ('SSB_ICD_GHH', 'SSB ICD GHH'), ('SSB_ICD_PT', 'SSB ICD PTT'), ('GZB_ICD_NOLI', 'GZB ICD NOLI'), ('GZB_ICD_MUZ', 'GZB ICD MUZ'), ('PNP_BMDJ', 'PNP BMDJ'), ('PNP_PCWD_DWNA', 'PNP PCWD DWNA')], default='TKD_ICD', max_length=15, null=True)),
                ('Module1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mod1', to='rakes.module')),
                ('Module2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mod2', to='rakes.module')),
                ('Module3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mod3', to='rakes.module')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
