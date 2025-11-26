from rest_framework import serializers
from .models import Clinic, Doctor, Patient, Consultation


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class ConsultationSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)

    doctor_id = serializers.PrimaryKeyRelatedField(
        source="doctor", queryset=Doctor.objects.all(), write_only=True
    )
    patient_id = serializers.PrimaryKeyRelatedField(
        source="patient", queryset=Patient.objects.all(), write_only=True
    )
    clinic_id = serializers.PrimaryKeyRelatedField(
        source="clinic", queryset=Clinic.objects.all(), write_only=True
    )

    class Meta:
        model = Consultation
        fields = [
            "id",
            "created_at",
            "start_time",
            "end_time",
            "status",
            "doctor",
            "patient",
            "clinic",
            "doctor_id",
            "patient_id",
            "clinic_id",
        ]
        read_only_fields = ("created_at",)

