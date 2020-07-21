# Generated by Django 3.0.7 on 2020-07-02 07:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0018_patientmodel_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
