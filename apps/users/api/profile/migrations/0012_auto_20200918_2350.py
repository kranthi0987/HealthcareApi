# Generated by Django 3.0.7 on 2020-09-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0011_userprofile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(blank=True, default='doctorprofile/defaultdoctor.jpg', null=True, upload_to='userprofile'),
        ),
    ]
