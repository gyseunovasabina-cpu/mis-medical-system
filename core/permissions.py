from rest_framework.permissions import BasePermission


class IsAdminDoctorPatientConsultationPermission(BasePermission):
    """
    Доступ на основе роли:
    - admin: полный доступ ко всем консультациям
    - doctor: доступ только к своим консультациям
    - patient: доступ только к своим консультациям
    """

    def has_permission(self, request, view):
        # Для всех запросов требуется авторизация
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Admin — полный доступ
        if user.role == "admin":
            return True

        # Doctor — доступ только к консультациям, где doctor == текущий доктор
        if user.role == "doctor" and hasattr(user, "doctor_profile"):
            return obj.doctor == user.doctor_profile

        # Patient — доступ только к своим консультациям
        if user.role == "patient" and hasattr(user, "patient_profile"):
            return obj.patient == user.patient_profile

        return False
