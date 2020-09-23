import uuid as uuid

from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime
from django.utils.timezone import now


class PatientModel(models.Model):
    # uuid = models.UUIDField(unique=False, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150, help_text="First Name of the Patient")
    last_name = models.CharField(max_length=150, help_text="Last Name of the Patient", null=True, blank=True)
    dob = models.CharField(max_length=100, unique=False, blank=True)
    date_of_joined = models.DateTimeField(null=True, blank=True, default=datetime.now)
    profile_image = models.FileField(blank=True, null=True, upload_to='patientprofile/')
    gender = models.CharField(max_length=10, unique=False)
    mobile = models.CharField(max_length=14, unique=False)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=False)
    patient_op = models.CharField(max_length=25, unique=False, blank=True)
    profession = models.CharField(max_length=100, unique=False, blank=True)
    guardian_name = models.CharField(max_length=100, unique=False, blank=True)
    guardian_relation = models.CharField(max_length=100, unique=False, blank=True)
    marital_status = models.CharField(max_length=100, unique=False, blank=True)
    bgroup = models.CharField(max_length=100, unique=False, blank=True)
    bpresure = models.CharField(max_length=100, unique=False, blank=True, default='80')
    sugar = models.CharField(max_length=100, unique=False, blank=True)
    heartbeat = models.CharField(max_length=100, unique=False, blank=True, default='80')
    haemoglobin = models.CharField(max_length=100, unique=False, blank=True)
    injury = models.CharField(max_length=100, unique=False, blank=True)
    aadhar_no = models.CharField(max_length=100, unique=False, blank=True)
    address = models.CharField(max_length=200, unique=False, blank=True)
    height = models.CharField(max_length=20, unique=False, blank=True)
    weight = models.CharField(max_length=20, unique=False, blank=True)
    active = models.BooleanField(default=True, null=True)
    date = models.DateTimeField(default=datetime.now)
    treatment = models.CharField(max_length=100, unique=False, blank=True)
    doc_id = models.CharField(max_length=100, unique=False, blank=True)
    about = models.CharField(max_length=100, unique=False, blank=True)
    about_patient = models.CharField(max_length=100, unique=False, blank=True)

    def __str__(self):
        return self.first_name


class ImageModel(models.Model):
    images = models.ImageField(upload_to='patientoldrecords/')
    patient_old_records = models.ForeignKey(PatientModel, default=None, related_name='patient_old_records',
                                            on_delete=models.PROTECT)


class PatientLogModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    treatment = models.CharField(max_length=500, help_text="Treatment", null=True, blank=True)
    date_of_joined = models.DateTimeField(null=True, blank=True, default=datetime.now)
    created_on = models.DateTimeField(null=True, blank=True, default=datetime.now)
    consulted_on = models.DateTimeField(null=True, blank=True, default=datetime.now)
    log_documents = models.FileField(blank=True, null=True, upload_to='patientoldlogs/')
    session_log = models.CharField(blank=True, null=True, max_length=500, help_text="patient stream data")
    patient_id = models.CharField(max_length=500, help_text="patient id", null=True, blank=True)

    # patient_model =  models.ForeignKey(PatientModel,null=True, blank=True,related_name='patient_logs',
    #                                         on_delete=models.PROTECT)
    def __str__(self):
        return str(self.consulted_on)


class StudentModel(models.Model):
    stid = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, help_text="entername", null=True, blank=True)

    def __str__(self):
        return str(self.stid)


class studentimages(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    text = models.CharField(max_length=200, help_text="enter", null=True, blank=True)
    stid = models.ForeignKey(StudentModel, related_name='studentimages', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
