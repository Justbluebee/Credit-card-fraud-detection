# Generated by Django 5.0 on 2024-02-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_remove_systemsettings_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemsettings',
            name='automate',
            field=models.CharField(choices=[('all', 'Automate All Transactions'), ('location', 'automate by location')], max_length=100),
        ),
        migrations.AlterField(
            model_name='systemsettings',
            name='blacklist_add',
            field=models.CharField(choices=[('rejected alerts', 'add rejected alerts to the blacklist automatically'), ('false negatives', 'add false negatives to the blacklist automatically')], max_length=100),
        ),
        migrations.AlterField(
            model_name='systemsettings',
            name='report_add',
            field=models.CharField(choices=[('auto', 'automatically generate reports from allowed transactions'), ('redirect', 'redirect the user to manually create a report after allowing a flagged transaction'), ('none', 'do not redirect the user or generate a report automatically')], max_length=100),
        ),
    ]