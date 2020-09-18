from rest_framework import serializers

from apps.patients.models import PatientModel, PatientLogModel, ImageModel, StudentModel, studentimages


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = '__all__'

    # def to_representation(self, instance):
    #     return {
    #         "active": instance.active,
    #         "log_details": instance.patient_logs.values('id', 'description')
    #     }


class PatientLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientLogModel
        fields = '__all__'


class PatientOldRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'



class StudentImage(serializers.ModelSerializer):
    class Meta:
        model =studentimages
        fields = '__all__'


class Studentserilalizer(serializers.ModelSerializer):
    studentimages = StudentImage(read_only=True,many=True)
    class Meta:
        model =StudentModel
        fields = '__all__'
