from django.contrib import admin
from .models import User, Clinic, Doctor, Patient, Consultation

admin.site.register(User)
admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Consultation)
