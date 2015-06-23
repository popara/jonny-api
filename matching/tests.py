from fixures import *
from . import tasks as T
from freezegun import freeze_time
from datetime import datetime
from django.core import mail

job_id = "job_id"

def test_job_start(api, ok):
    r = api.post('/api/job/start/%s' % job_id)

    assert r.status_code == ok
    assert r.data == job_id

def test_applying_for_job(api, ok, get_job, patch_job, fresh_job):
    fresh_job(job_id)
    user = "simplelogin:3"
    r = api.post('/api/job/apply/%s/%s' % (job_id, user))

    assert r.status_code == ok
    assert 'first' in r.data

    j = get_job(job_id)

    assert len(j['applicants']) == 1

def test_applying_for_job_nd(api, ok, get_job, patch_job, fresh_job):
    fresh_job(job_id)
    user = "simplelogin:3"
    user2 = "simplelogin:4"
    r = api.post('/api/job/apply/%s/%s' % (job_id, user))
    r2 = api.post('/api/job/apply/%s/%s' % (job_id, user2))

    assert r.status_code == ok
    assert r2.status_code == ok
    assert 'second' in r2.data

    j = get_job(job_id)

    assert len(j['applicants']) == 2


def test_getting_expert(available_experts):
    u = T.get_experts()
    assert checkEqual(available_experts, u)
    assert len(u) == 1
    assert u[0]['id'] == 'simplelogin:1'

def test_sending_emails():
    e1 = "test@test.te"
    ex1 = {"name": "Joe", "email": e1, "id": "simplelogin:1"}
    m = T.dispatch_initial_email(job_id, ex1)
    m1 = mail.outbox[0]

    assert len(mail.outbox) == 1
    assert m1.to == [e1]

def test_notify_experts(available_experts):
    m = T.notify_experts(available_experts, job_id)
    assert len(available_experts) == len(mail.outbox)

def test_hard_limit_no_applicants(get_job, patch_job):
    patch_job(job_id, {'applicants': []})
    T.hard_limit(job_id)
    j = get_job(job_id)

    #teardown
    patch_job(job_id, {'applicants': []})

    assert len(mail.outbox) == 2
    assert len(j['applicants']) == 1

def test_hard_limit_with_applicants(get_job, patch_job):
    A = 'applicants'
    apl = {"user_id": "simplelogin:1"}
    patch_job(job_id, {A: [apl]})
    T.hard_limit(job_id)
    j = get_job(job_id)

    #teardown
    patch_job(job_id, {'applicants': []})

    assert len(mail.outbox) == 0
    assert len(j['applicants']) == 1
