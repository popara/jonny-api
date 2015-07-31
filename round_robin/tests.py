from fixures import *
from cache_model import get_next, get_current, increment_state, ROBIN_STATE_KEY

def test_current(cache):
    assert get_current() is None or get_current() is 0
    cache.set(ROBIN_STATE_KEY, 1)
    assert get_current() is 1

def test_incrementing():
    start = 1
    assert increment_state(start) is start+1

    curr =  get_current()
    assert curr is start+1

    assert increment_state(curr) is curr+1
    assert get_current() is curr+1

def test_rounding():
    start = 0
    increment_state(start)

    assert get_next() is 2
    assert get_next() is 3
    assert get_next() is 0
    assert get_next() is 1
    assert get_next() is 2
    assert get_next() is 3
    assert get_next() is 0
    assert get_next() is 1


def test_api_rounding(api, cache):
    cache.delete("ROBIN_LIMIT_KEY")
    cache.delete("ROBIN_STATE_KEY")

    result = api.get('/api/round_robin')
    assert result.data is 0

    result = api.get('/api/round_robin')
    assert result.data is 1

    result = api.get('/api/round_robin')
    assert result.data is 2

    result = api.get('/api/round_robin')
    assert result.data is 3

    result = api.get('/api/round_robin')
    assert result.data is 0
