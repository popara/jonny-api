from __future__ import absolute_import
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from firestone import get_experts as fb_get_experts, \
    FireRoot, get_job, tstamp, get_backup_experts, patch_job, get_user, \
    APPLICANTS_KEY

def job_application(user_id):
    return {
        "user_id": user_id,
        "applied": tstamp()
    }

job_start_subject = "Jonny"
HARD_LIMIT_PERIOD = settings.HARD_LIMIT_PERIOD
SOFT_LIMIT_PERIOD = settings.SOFT_LIMIT_PERIOD
QUEUE_SIZE = settings.QUEUE_SIZE

e_from = "Mr. Wolf <%s>" % settings.MR_WOLF_EMAIL



def job_start_text(job_id):
    return "Hey Jonny, react! %s" % job_id


def dispatch_initial_email(job_id, expert):
    return send_mail(job_start_subject, job_start_text(job_id), e_from, [expert['email']])


@shared_task
def start_hard_limit(job_id):
    return hard_limit.apply_async(args=[job_id], countdown=HARD_LIMIT_PERIOD)

@shared_task
def hard_limit(job_id):
    job = get_job(job_id)
    if APPLICANTS_KEY not in job or len(job[APPLICANTS_KEY]) == 0:
        backs = get_backup_experts()
        aps = map(lambda a: job_application(a['id']), backs)
        patch_job(job_id, {APPLICANTS_KEY: aps})
        final_emails(job_id)


@shared_task
def get_user_by_id(user_id):
    return get_user(user_id)


@shared_task
def apply_for_job(user_id, job_id):
    job = get_job(job_id)
    if APPLICANTS_KEY not in job:
        job[APPLICANTS_KEY] = []

    appls = job[APPLICANTS_KEY] + [job_application(user_id)]
    patch_job(job_id, {APPLICANTS_KEY: appls})

@shared_task
def set_soft_limit(job_id):
    job = get_job(job_id)
    if APPLICANTS_KEY not in job or len(job[APPLICANTS_KEY]) == 0:
        soft_limit.apply_async(args=[job_id], countdown=SOFT_LIMIT_PERIOD)


@shared_task
def soft_limit(job_id):
    job = get_job(job_id)
    user = get_user(job['owner'])

    send_mail("Soft User", "User is done", e_from, [user['email']])


@shared_task
def get_experts():
    return fb_get_experts()


@shared_task
def notify_experts(experts, job_id):
    for expert in experts:
        dispatch_initial_email(job_id, expert)

@shared_task
def final_emails(job_id):
    j = get_job(job_id)
    owner = get_user(j['owner'])
    experts = map(lambda a: get_user(a['user_id']), j['applicants'])
    send_mail("final user", "final body body", e_from, [owner['email']])

    for e in experts:
        send_mail("final user", "final body body", e_from, [e['email']])
