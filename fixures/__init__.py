import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.conf import settings

@pytest.fixture
def api():
    return APIClient()

@pytest.fixture
def ok():
    return status.HTTP_200_OK

@pytest.fixture
def settings():
    return settings 
