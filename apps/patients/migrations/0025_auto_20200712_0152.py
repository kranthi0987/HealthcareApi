# Generated by Django 3.0.7 on 2020-07-11 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0024_auto_20200712_0150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientmodel',
            old_name='bGroup',
            new_name='bgroup',
        ),
        migrations.RenameField(
            model_name='patientmodel',
            old_name='bPresure',
            new_name='bpresure',
        ),
    ]
