import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.models import User


@pytest.mark.django_db
def test_consultation_list_requires_auth():
    client = APIClient()
    url = reverse("consultation-list")
    response = client.get(url)
    assert response.status_code == 401
