import uuid as uuid

from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class PatientLogModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=500, help_text="log description", null=True, blank=True)
    date_of_joined = models.DateTimeField(null=True, blank=True, default=datetime.now)
    created_on = models.DateTimeField(null=True, blank=True, default=datetime.now)
    consulted_on = models.DateTimeField(null=True, blank=True, default=datetime.now)
    log_documents = models.FileField(blank=True, null=True, upload_to='patientlogs/')
    patient_uuid = models.CharField(max_length=500, help_text="patient id", null=True, blank=True)

    def __str__(self):
        return self.consulted_on


class PatientModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150, help_text="First Name of the Patient")
    last_name = models.CharField(max_length=150, help_text="Last Name of the Patient", null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    date_of_joined = models.DateTimeField(null=True, blank=True, default=datetime.now)
    patientprofile = models.FileField(blank=True, null=True, upload_to='patientprofile/')
    gender = models.CharField(max_length=10, unique=False)
    mobile_number = models.CharField(max_length=14, unique=False)
    email_id = models.EmailField(max_length=70, null=True, blank=True, unique=False)
    patient_op_id = models.CharField(max_length=25, unique=False, blank=True)
    profession = models.CharField(max_length=100, unique=False, blank=True)
    guardian_name = models.CharField(max_length=100, unique=False, blank=True)
    guardian_relation = models.CharField(max_length=100, unique=False, blank=True)
    aadhar_no = models.CharField(max_length=100, unique=False, blank=True)
    address = models.CharField(max_length=200, unique=False, blank=True)
    height = models.CharField(max_length=20, unique=False, blank=True)
    weight = models.CharField(max_length=20, unique=False, blank=True)
    active = models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.first_name


class ImageModel(models.Model):
    images = models.ImageField(upload_to='patientoldrecords/')
    patient_old_records = models.ForeignKey(PatientModel, default=None, related_name='patient_old_records',
                                            on_delete=models.PROTECT)