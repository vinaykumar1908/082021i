# Generated by Django 3.2.6 on 2021-08-28 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mnpComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('upload', models.FileField(blank=True, null=True, upload_to='uploadsMnpComments/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='mnpPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('upload', models.FileField(blank=True, null=True, upload_to='uploadsMnp/%Y/%m/%d/')),
            ],
        ),
    ]
