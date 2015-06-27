from __future__ import absolute_import
from celery import shared_task

from firestone import get_experts as fb_get_experts, \
    FireRoot, get_job, get_backup_experts, patch_job, get_user, \
    APPLICANTS_KEY

from firestone.models import job_application, apply_for_job as afj, \
    finish_drafting, has_space, \
    HARD_LIMIT_PERIOD, SOFT_LIMIT_PERIOD, QUEUE_SIZE

from .models import JobStatus, apply_for_job_url, fe_user_pick, \
    get_details
from .emails import job_start_expert, job_done_client


def dispatch_initial_email(job_id, expert, details):
    link = apply_for_job_url(job_id, expert['id'])
    return job_start_expert(expert, details, link)

@shared_task
def start_drafting(job_id):
    return patch_job(job_id, {'status': JobStatus.drafting})


@shared_task
def start_hard_limit(job_id):
    hard_limit.apply_async(args=[job_id], countdown=HARD_LIMIT_PERIOD())
    return "Hard Limit scheduled in %s" % HARD_LIMIT_PERIOD()

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
        apl = afj(job_id, job, user_id)
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
    print job
    status = job['status']

    if status == JobStatus.drafting:
        finish_drafting(job_id)
        return "Sent %s mail" % job_done_client(user, fe_user_pick())
    else:
        return "Soft Limit already reached"

@shared_task
def get_experts():
    return fb_get_experts()

@shared_task
def notify_experts(experts, job_id):
    job = get_job(job_id)
    details = get_details(job['owner'])
    for expert in experts:
        dispatch_initial_email(job_id, expert, details)

@shared_task
def final_emails(job_id):
    j = get_job(job_id)
    owner = get_user(j['owner'])
    job_done_client(owner, fe_user_pick())
