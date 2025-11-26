from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Consultation
from .serializers import ConsultationSerializer
from .permissions import IsAdminDoctorPatientConsultationPermission


class ConsultationViewSet(viewsets.ModelViewSet):
    """
    CRUD + фильтрация + поиск + сортировка + смена статуса.
    """
    queryset = Consultation.objects.all().select_related("doctor", "patient", "clinic")
    serializer_class = ConsultationSerializer
    permission_classes = [IsAdminDoctorPatientConsultationPermission]

    # Поиск и сортировка
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "doctor__last_name",
        "doctor__first_name",
        "patient__last_name",
        "patient__first_name",
    ]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        """
        Фильтрация по статусу + ограничение доступа по роли.
        """
        qs = super().get_queryset()
        user = self.request.user

        # Фильтр по статусу ?status=pending
        status_param = self.request.query_params.get("status")
        if status_param:
            qs = qs.filter(status=status_param)

        # Admin — видит все консультации
        if user.role == "admin":
            return qs

        # Doctor — видит только свои консультации
        if user.role == "doctor" and hasattr(user, "doctor_profile"):
            return qs.filter(doctor=user.doctor_profile)

        # Patient — только свои консультации
        if user.role == "patient" and hasattr(user, "patient_profile"):
            return qs.filter(patient=user.patient_profile)

        return qs.none()

    @action(detail=True, methods=["post"])
    def change_status(self, request, pk=None):
        """
        POST /api/consultations/<id>/change_status/
        Body: { "status": "started" }
        """
        consultation = self.get_object()
        new_status = request.data.get("status")

        if not new_status:
            return Response({"error": "status is required"}, status=status.HTTP_400_BAD_REQUEST)

        consultation.status = new_status
        consultation.save(update_fields=["status"])

        return Response(self.get_serializer(consultation).data)
