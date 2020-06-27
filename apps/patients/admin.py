from django.contrib import admin

# Register your models here.
from apps.patients.models import PatientModel

admin.site.register(PatientModel)