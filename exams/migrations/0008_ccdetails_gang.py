# Generated by Django 3.2.6 on 2021-09-16 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20210911_1625'),
        ('exams', '0007_alter_ccdetails_rakename'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccdetails',
            name='Gang',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='v2comments', to='staff.gang'),
        ),
    ]
