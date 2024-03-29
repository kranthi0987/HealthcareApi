# Generated by Django 3.0.7 on 2020-06-22 19:40

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('description', models.CharField(blank=True, help_text='log description', max_length=500, null=True)),
                ('date_of_joined', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('created_on', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('consulted_on', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('log_documents', models.FileField(blank=True, null=True, upload_to='patientlogs/')),
            ],
        ),
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(help_text='First Name of the Patient', max_length=150)),
                ('last_name', models.CharField(blank=True, help_text='Last Name of the Patient', max_length=150, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('date_of_joined', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('patientprofile', models.FileField(blank=True, null=True, upload_to='patientprofile/')),
            ],
        ),
        migrations.DeleteModel(
            name='Patients',
        ),
    ]
