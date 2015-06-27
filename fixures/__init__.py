import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.conf import settings
from .firebase_fixutres import *
from .game import *

@pytest.fixture
def api():
    return APIClient()

@pytest.fixture
def ok():
    return status.HTTP_200_OK

@pytest.fixture
def settings():
    return settings


def checkEqual(L1, L2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)
