# Generated by Django 3.0.7 on 2020-06-26 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20200623_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmodel',
            name='patient_log',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.PatientLogModel'),
        ),
    ]