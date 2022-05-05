# Generated by Django 4.0.3 on 2022-05-05 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_request_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rejectiontable',
            name='reject_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rejection_table_rejected_by', to=settings.AUTH_USER_MODEL),
        ),
    ]