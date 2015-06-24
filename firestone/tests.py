from fixures import *
from django.conf import settings
settings.FIREBASE = 'jonny-test'
from firestone import get_job, patch_job, get_backup_experts
from firestone.models import has_space


def test_backup_experts():
    es = get_backup_experts()
    assert len(es) == 1
    j = es[0]
    assert j["email"] == "zeljko@jonnyibiza.com"

def test_saving():
    job_id = 'job_id'
    j = get_job(job_id)
    patch_job(job_id, {'applicants': {}})

def test_has_space():
    k = 'applicants'
    a = {}
    assert has_space(a)
    a = {k: []}
    assert has_space(a)
    a = {k: [{}, {}]}
    assert has_space(a)
    a = {k: [{}, {}, {}]}
    assert not has_space(a)
