import pytest
from funcy import merge
from firebase import firebase as f
from django.conf import settings
from firestone import fb_url, get_job as fjob, merge_ids, patch_job as pj, put_job
from firestone.models import apply_for_job

@pytest.fixture
def fire_app(test_firebase):
    fauth = f.FirebaseAuthentication(settings.FIREBASE_SECRET, settings.MR_WOLF_EMAIL, admin=True, debug=True)
    return f.FirebaseApplication(fb_url(settings.FIREBASE), fauth)

@pytest.fixture
def available_experts(fire_app):
    exp_ids = fire_app.get('/experts', None)
    us = [fire_app.get('/users', k) for k in exp_ids.keys()]
    us = merge_ids(exp_ids, us)
    return filter(lambda u: u['available'], us)

# {u'simplelogin:2': True, u'simplelogin:1': True}

@pytest.fixture
def get_job(fire_app):
    return fjob

@pytest.fixture
def patch_job():
    return pj

@pytest.fixture
def fresh_job(patch_job):
    def fn(job_id):
        patch_job(job_id, {'applicants': [], 'status': 'drafting'})

    return fn

@pytest.fixture
def super_fresh_job(patch_job):
    def fn(job_id):
        put_job(job_id, {'owner': job_id})

    return fn

@pytest.fixture
def apply_for_job():
    return apply_for_job

@pytest.fixture
def test_firebase():
    return 'jonny-test'

@pytest.fixture
def empty_job():
    return {
        "owner": "sample:1",
        "status": "drafting"
    }

@pytest.fixture
def applied_job(empty_job):
    return merge(empty_job, {
        "applicants": [{}, {}]
    })

@pytest.fixture
def full_job(empty_job):
    return merge(empty_job, {
        "applicants": [{}, {}, {}],
        "status": "drafted"
    })
