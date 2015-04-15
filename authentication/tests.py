import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

TEST_EMAIL = 'test@email.com'
TEST_PASSWORD = 'peradetlc'
def url(body):
  return "/api/account/%s" % body

@pytest.fixture
def api():
  return APIClient()

@pytest.mark.django_db
def test_registration(api):
  assert User.objects.filter(email=TEST_EMAIL).count() == 0

  r = api.post(url('register'), {
    'email': TEST_EMAIL,
    'password': TEST_PASSWORD
  })

  assert r.status_code == 201

  assert User.objects.filter(email=TEST_EMAIL).count() == 1