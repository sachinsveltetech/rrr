# Generated by Django 4.0.3 on 2022-05-19 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_request_form', '0012_userrequestform_updated_date_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrequestform',
            name='updated_date_at',
        ),
        migrations.RemoveField(
            model_name='userrequestform',
            name='updated_time_at',
        ),
        migrations.AddField(
            model_name='userrequestform',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]