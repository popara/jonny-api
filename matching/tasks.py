from __future__ import absolute_import
from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail

from firestone import get_experts as fb_get_experts, \
    FireRoot, get_job, get_backup_experts, patch_job, get_user, \
    APPLICANTS_KEY

from firestone.models import job_application, apply_for_job as afj, \
    finish_drafting, has_space, \
    HARD_LIMIT_PERIOD, SOFT_LIMIT_PERIOD, QUEUE_SIZE

job_start_subject = "Jonny"

e_from = "Mr. Wolf <%s>" % settings.MR_WOLF_EMAIL


def job_start_text(job_id):
    return "Hey Jonny, react! %s" % job_id


def dispatch_initial_email(job_id, expert):
    return send_mail(job_start_subject, job_start_text(job_id), e_from, [expert['email']])

@shared_task
def start_drafting(job_id):
    return patch_job(job_id, {'status': 'drafting'})


@shared_task
def start_hard_limit(job_id):
    return hard_limit.apply_async(args=[job_id], countdown=HARD_LIMIT_PERIOD())

@shared_task
def hard_limit(job_id):
    job = get_job(job_id)

    if APPLICANTS_KEY not in job or len(job[APPLICANTS_KEY]) == 0:
        backs = get_backup_experts()
        aps = map(lambda a: job_application(a['id']), backs)
        patch_job(job_id, {APPLICANTS_KEY: aps})
        finish_drafting(job_id)
        return final_emails(job_id)


@shared_task
def get_user_by_id(user_id):
    return get_user(user_id)


@shared_task
def apply_for_job(user_id, job, job_id):
    if has_space(job):
        afj(job_id, user_id)

        job = get_job(job_id)
        if len(job[APPLICANTS_KEY]) == QUEUE_SIZE():
            soft_limit(job_id)

        return job
    else:
        raise Exception("No more space")


@shared_task
def start_soft_limit(job_id, period):
    job = get_job(job_id)
    if APPLICANTS_KEY in job and len(job[APPLICANTS_KEY]) == 1:
        soft_limit.apply_async(args=[job_id], countdown=period)
        return "Soft Limit zakazan za: %s" % period
    else:
        return "Nema potrebe za novim Soft Limitom"


@shared_task
def soft_limit(job_id):
    job = get_job(job_id)
    user = get_user(job['owner'])
    status = job['status']

    if status == 'drafting':
        finish_drafting(job_id)
        r = send_mail("Soft User", "User is done", e_from, [user['email']])
        return "Sent %s mail" % r
    else:
        return "Soft Limit already reached"

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
