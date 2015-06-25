from . import get_job, APPLICANTS_KEY, tstamp, patch_job
from django.conf import settings

class JobApplication:
    def __init__(self, user_id, at):
        self.user_id = user_id
        self.applied = at


class JobJob:
    def __init__(self, owner):
        self.owner = owner
        self.applicants = []


def job_application(user_id):
    return {
        "user_id": user_id,
        "applied": tstamp()
    }

def finish_drafting(job_id):
    patch_job(job_id, {'status':'drafted'})


def job_queue_position(job):
    if APPLICANTS_KEY in job:
        return len(job[APPLICANTS_KEY])
    else:
        return 0

def job_queue_position_words(pos):
    if pos <= QUEUE_SIZE():
        return position_word(pos)
    else:
        return "Full"

def position_word(post):
    if post == 1:
        return 'first'
    elif post == 2:
        return 'second'
    elif post == 3:
        return 'third'
    elif post == 4:
        return 'fourth'

def order_word(post):
    if post == 1:
        return '1st'
    elif post == 2:
        return '2nd'
    elif post == 3:
        return '3rd'
    elif post == 4:
        return '4th'


def apply_for_job(job_id, job, user_id):
    if APPLICANTS_KEY not in job:
        job[APPLICANTS_KEY] = []

    user_application = job_application(user_id)
    if user_application not in job[APPLICANTS_KEY]:
        appls = job[APPLICANTS_KEY] + [user_application]
        patch_job(job_id, {APPLICANTS_KEY: appls})

    return user_application

def has_space(job):
    return (APPLICANTS_KEY not in job) or \
        (APPLICANTS_KEY in job and len(job[APPLICANTS_KEY]) < QUEUE_SIZE())

def job_drafting(job_id):
    job = get_job(job_id)
    return 'status' in job and (job['status'] is 'drafting' or job['status'] is 'drafted')


def has_applied(job, user_id):
    return (APPLICANTS_KEY in job) and \
        (user_id in map(lambda a: a['user_id'], job[APPLICANTS_KEY]))


def HARD_LIMIT_PERIOD(): return settings.HARD_LIMIT_PERIOD

def SOFT_LIMIT_PERIOD(): return settings.SOFT_LIMIT_PERIOD

def QUEUE_SIZE(): return settings.QUEUE_SIZE
