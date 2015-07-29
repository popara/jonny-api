from django.core.cache import cache
ROBIN_STATE_KEY = "ROBIN_STATE_KEY"
ROBIN_LIMIT_KEY = "ROBIN_LIMIT_KEY"
ROBIN_LIMIT = 4
ROBIN_START = 0

def get_current():
    return cache.get(ROBIN_STATE_KEY)

def reset_robin():
    cache.set(ROBIN_STATE_KEY, ROBIN_START)
    return ROBIN_START

def setup_robin():
    cache.set(ROBIN_LIMIT_KEY, ROBIN_LIMIT)
    cache.set(ROBIN_STATE_KEY, ROBIN_START)
    cache.persist(ROBIN_LIMIT_KEY)
    cache.persist(ROBIN_STATE_KEY)

def safe_limit():
    if cache.get(ROBIN_LIMIT_KEY) is None:
        setup_robin()

    return cache.get(ROBIN_LIMIT_KEY)

def over_limit(state):
    return (state >= safe_limit() -1) or state is None


def increment_state(state):
    s = state + 1
    cache.set(ROBIN_STATE_KEY, s)
    return s

def get_next():
    current = get_current()
    if over_limit(current):
        return reset_robin()
    else:
        return increment_state(current)
