# Generated by Django 4.0.3 on 2022-05-19 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_request_form', '0015_alter_userrequestform_updated_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrequestform',
            old_name='updated_by',
            new_name='updated_by_tsp',
        ),
    ]