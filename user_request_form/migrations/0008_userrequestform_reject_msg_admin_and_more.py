# Generated by Django 4.0.3 on 2022-05-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_request_form', '0007_remove_userrequestform_date_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequestform',
            name='reject_msg_admin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userrequestform',
            name='reject_msg_tsp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
