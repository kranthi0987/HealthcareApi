# Generated by Django 3.0.7 on 2020-09-10 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0032_remove_patientmodel_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientmodel',
            old_name='img',
            new_name='profile_image',
        ),
    ]
