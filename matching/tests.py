from fixures import *
from freezegun import freeze_time
from datetime import datetime
from time import sleep
from django.core import mail
from django.conf import settings
from funcy import is_list, all, str_join
from . import tasks as T
import fixures
from .models import JobStatus, job_status, get_questions, get_anon, \
    get_anons_answers, get_details, zipthem, answer_as_str



job_id = "simplelogin:190"
def data(r):
    return r.content

def job_start(api, job_id):
    return api.post('/api/job/start/%s' % job_id)


def job_apply(api, job_id, user_id):
    return api.get('/api/job/apply/%s/%s' % (job_id, user_id))


def test_job_start(api, ok, get_job, super_fresh_job, fire_app):
    status = 'status'

    super_fresh_job(job_id)
    job = get_job(job_id)
    assert status not in job

    r = job_start(api, job_id)
    sleep(14)
    assert r.status_code == ok
    assert r.data == job_id

    j = get_job(job_id)
    assert j[status] == 'drafting'

def test_applying_for_job(api, ok, get_job, patch_job, fresh_job):
    fresh_job(job_id)
    user = "simplelogin:3"
    r = job_apply(api, job_id, user)
    sleep(2)
    assert r.status_code == ok
    assert 'first' in data(r)

    j = get_job(job_id)

    assert len(j['applicants']) == 1

def test_applying_for_job_nd(api, ok, get_job, patch_job, fresh_job):
    fresh_job(job_id)
    user = "simplelogin:3"
    user2 = "simplelogin:4"
    user3 = "simplelogin:5"
    r = job_apply(api, job_id, user)
    r2 = job_apply(api, job_id, user2)
    r3 = job_apply(api, job_id, user3)
    assert r.status_code == ok
    assert r2.status_code == ok
    assert r3.status_code == ok
    assert 'first' in data(r)
    assert 'second' in data(r2)
    assert 'third' in data(r3)

    j = get_job(job_id)
    assert len(j['applicants']) == 3

def test_already_applied(api, ok, get_job, patch_job, fresh_job):
    fresh_job(job_id)
    user = "simplelogin:3"

    r = job_apply(api, job_id, user)

    assert r.status_code == ok
    assert 'first' in data(r)

    j = get_job(job_id)
    assert len(j['applicants']) == 1


    r = job_apply(api, job_id, user)
    assert r.status_code == ok
    assert 'already' in data(r)

    j = get_job(job_id)
    assert len(j['applicants']) == 1


def test_getting_expert(available_experts):
    u = T.get_experts()
    assert len(u) > 1

def test_sending_emails():
    e1 = "test@test.te"
    ex1 = {"name": "Joe", "email": e1, "id": "simplelogin:1"}
    m = T.dispatch_initial_email(job_id, ex1, {})
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

    assert len(mail.outbox) == 1
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

def test_soft_limit_expires(api, get_job, fresh_job, apply_for_job):
    fresh_job(job_id)
    A = 'applicants'
    u1 = "simplelogin:1"
    u2 = "simplelogin:2"

    r = job_apply(api, job_id, u1)
    r2 = job_apply(api, job_id, u2)

    assert len(mail.outbox) == 0
    j = get_job(job_id)
    assert j["status"] == "drafting"
    T.soft_limit(job_id)

    assert len(mail.outbox) == 1
    m1 = mail.outbox[0]

    assert m1.to == ['zeljko@jonnyibiza.com']


def test_queue_filled(api, ok, get_job, fresh_job, apply_for_job):
    fresh_job(job_id)
    settings.SOFT_LIMIT_PERIOD = 2

    def u(id):
        return "simplelogin:%s" % id

    for applicant in range(0, settings.QUEUE_SIZE):
        job_apply(api, job_id, u(applicant+1))

    r = job_apply(api, job_id, u(settings.QUEUE_SIZE+2))
    assert r.status_code != ok
    assert "too late" in data(r)

def test_job_state(empty_job, applied_job, full_job):
    assert empty_job["status"] == JobStatus.drafting


def test_getting_questions():
    fields = ['id', 'name', 'category', 'text', 'type', 'label']
    qs = get_questions()
    def is_q(q):
        return all(map(lambda x: x in q, fields))

    assert is_list(qs)
    assert all(map(is_q, qs))


def test_get_anon_answers():
    a = "anonymous:-Jr8CygRdKAANrQ5ENax"
    fields = ['at', 'value', 'id']
    ans = get_anons_answers(a)
    def is_ans(an):
        return all(map(lambda x: x in an, fields))
    assert is_list(ans)
    assert all(map(is_ans, ans))

def test_match_questions():
    ans  = [{'id': 'a', 'value': 'aa'}, {'id': 'b', 'value': 'bb'}]
    qs = [{'id': 'a', 'text': 'what', 'type': 'freeform'}, {'id': 'b', 'text': 'who', 'type': 'bingo'}]

    r = zipthem(qs, ans)
    fields = ['question', 'answer']
    def is_z(z):
        return all(map(lambda a: a in z, fields))

    assert is_list(r)
    assert all(map(is_z, r))

def test_zippingthem(questions, user_answers):
    r = zipthem(questions, user_answers)

    assert is_list(r)

def test_answer_as_string(typed_answers):
    AT = typed_answers
    keys = AT.keys()
    o = AT['checklist']['value']
    t = 'check-list'
    v  = answer_as_str(o, t)
    assert v == str_join(', ', o)

    o = AT['checklist_2']['value']
    v = answer_as_str(o, t)
    assert 'Somez, Thingzsz'

    o = AT['bingo']['value']
    v = answer_as_str(o, 'bingo')
    assert v == str_join(', ', o)

    o = AT['about']['value']
    v = answer_as_str(o, 'about')
    assert v == 'male, 31, straight'

    o = AT['companydetails']['value']
    v = answer_as_str(o, 'company-details')

    assert '3 Boys' in v
    assert '34 Girls' in v
    assert 'partner' not in v
    assert 'Male friends: 4' in v

    o = AT['rolling']['value']
    v = answer_as_str(o, 'rolling')
    assert 'Rock star!' == v

    o = AT['dates']['value']
    v  = answer_as_str(o, 'dates')
    assert 'To June 24' in v
    assert 'flexible' in v

    o = AT['freeform']['value']
    v = answer_as_str(o, 'freeform')
    assert v == 'Knock the blast'

def test_dummy(fire_app):
    assert fire_app.get('/levels', None)
    assert fire_app.get('/users', 'simplelogin:190')
