from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        DOCTOR = "doctor", "Doctor"
        PATIENT = "patient", "Patient"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.PATIENT)


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    legal_address = models.CharField(max_length=255)
    physical_address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField("core.User", on_delete=models.CASCADE, related_name="doctor_profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=255)
    clinics = models.ManyToManyField(Clinic, related_name="doctors")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Patient(models.Model):
    user = models.OneToOneField("core.User", on_delete=models.CASCADE, related_name="patient_profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Consultation(models.Model):
    class Status(models.TextChoices):
        CONFIRMED = "confirmed", "Подтверждена"
        PENDING = "pending", "Ожидает"
        STARTED = "started", "Начата"
        FINISHED = "finished", "Завершена"
        PAID = "paid", "Оплачена"

    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="consultations")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="consultations")
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="consultations")

    def __str__(self):
        return f"{self.doctor} -> {self.patient} ({self.start_time})"

