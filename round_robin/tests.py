from fixures import *
from models import get_next, RoundRobin

@pytest.fixture
def roundrobin():
    return RoundRobin.objects.create(state=0, limit=4)

@pytest.mark.django_db
def test_rounding(roundrobin):
    r = roundrobin.id

    assert get_next(r) is 1
    assert get_next(r) is 2
    assert get_next(r) is 3
    assert get_next(r) is 0
    assert get_next(r) is 1
    assert get_next(r) is 2
    assert get_next(r) is 3
    assert get_next(r) is 0

@pytest.mark.django_db
def test_api_rounding(api, roundrobin):
    url = '/api/round_robin/%s' % roundrobin.id

    result = api.get(url)
    assert result.data is 1

    result = api.get(url)
    assert result.data is 2

    result = api.get(url)
    assert result.data is 3

    result = api.get(url)
    assert result.data is 0
