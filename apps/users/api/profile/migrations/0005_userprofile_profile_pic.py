# Generated by Django 3.0.7 on 2020-06-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20200527_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to='profilepics/'),
        ),
    ]
