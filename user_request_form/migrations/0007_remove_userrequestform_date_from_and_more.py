# Generated by Django 4.0.3 on 2022-05-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_request_form', '0006_remove_userrequestform_tsp_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrequestform',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='userrequestform',
            name='date_to',
        ),
        migrations.RemoveField(
            model_name='userrequestform',
            name='time_from',
        ),
        migrations.RemoveField(
            model_name='userrequestform',
            name='time_to',
        ),
        migrations.AddField(
            model_name='ipport',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ipport',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ipport',
            name='time_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ipport',
            name='time_to',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
