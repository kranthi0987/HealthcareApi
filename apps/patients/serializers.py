from rest_framework import serializers

from apps.patients.models import PatientModel, PatientLogModel, ImageModel


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
