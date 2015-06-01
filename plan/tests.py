import pytest
from fixures import *




@pytest.mark.django_db
def test_charge_get(api, ok):
    r = api.get('/api/charge')

    assert r.status_code == ok
    assert r.data == ":)"
