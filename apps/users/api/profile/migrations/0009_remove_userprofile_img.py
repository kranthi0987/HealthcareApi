# Generated by Django 3.0.7 on 2020-07-12 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0008_auto_20200713_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='img',
        ),
    ]