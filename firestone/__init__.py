from firebase import firebase
from django.conf import settings
from funcy import mapcat, walk
from time import time

import logging
logger = logging.getLogger('workers')

APPLICANTS_KEY = 'applicants'

def fb_url(base):
    return "https://%s.firebaseio.com/" % base

FireRoot = firebase.FirebaseApplication(fb_url(settings.FIREBASE))

def get_job(id):
    return FireRoot.get('/jobs', id)

def patch_job(id, data):
    return FireRoot.patch('/jobs/%s' % id, data)

def put_job(id, data):
    return FireRoot.put('/jobs/', id, data)

def get_user(id):
    u = FireRoot.get('/users', id)
    u['id'] = id
    return u

def get_backup_experts():
    be = FireRoot.get('/backup_experts', None)
    ids = mapcat(lambda x: x.keys(), be)
    return [get_user(i) for i in ids]


def get_experts():
    logger.info(FireRoot.dsn)
    exp_ids = FireRoot.get('/experts', None)
    us = [get_user(k) for k in exp_ids.keys()]
    print us
    return filter(lambda u: u['available'], us)


def merge_id(key, val):
    val['id'] = key
    return (key, val)


def merge_ids(ids, collection):
    return map(lambda i: i[1],
        walk(lambda x: merge_id(*x), zip(ids, collection))
    )

def tstamp():
    return int(time() * 1000)
