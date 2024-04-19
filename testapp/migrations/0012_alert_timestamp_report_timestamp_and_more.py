# Generated by Django 5.0 on 2024-02-25 09:47

from django.db import migrations, models
from django.utils import timezone  

class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_alter_systemsettings_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
    ]