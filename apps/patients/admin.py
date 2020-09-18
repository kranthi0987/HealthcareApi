from django.contrib import admin

# Register your models here.
from apps.patients.models import PatientModel, studentimages, StudentModel

admin.site.register(PatientModel)

admin.site.register(StudentModel)
admin.site.register(studentimages)