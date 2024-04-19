# Generated by Django 5.0 on 2024-02-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_rename_location_systemsettings_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemsettings',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='systemsettings',
            name='settings_class',
            field=models.CharField(default='general', max_length=20),
        ),
    ]