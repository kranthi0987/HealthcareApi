# Generated by Django 3.0.7 on 2020-09-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0022_userprofile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
