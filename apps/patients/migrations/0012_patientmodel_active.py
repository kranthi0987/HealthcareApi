# Generated by Django 3.0.7 on 2020-06-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_auto_20200627_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmodel',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]