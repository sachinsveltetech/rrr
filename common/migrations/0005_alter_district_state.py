# Generated by Django 4.0.3 on 2022-05-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_tsp_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.CharField(default='ASSAM', max_length=200),
        ),
    ]