# Generated by Django 3.0.6 on 2020-05-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20200527_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
