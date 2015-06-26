from firestone import get_user
from django.core.urlresolvers import reverse

class JobStatus:
    drafting = "drafting"
    drafted = "drafted"
    selected = "selected"

def job_status(job):
    return job['status']

def user_selected(job, user_id):
    return (job['status'] is JobStatus.selected) and \
        (get_user(job['owner'])['expert'] == user_id)

def job_applied_status(job, user_id):

    still_in_progress = (job_status(job) == JobStatus.drafting)
    selected = not still_in_progress and \
        (user_selected(job, user_id))
    done_not_selected = not selected
    done_selected = selected
    print "in progres %s " % still_in_progress
    print "done"
    return {
        'in_progress': still_in_progress,
        'done_selected': done_selected,
        'done_not_selected': done_not_selected,
    }

def base(rest):
    return "https://jonnyibiza.com/%s" % rest

def fe_expert(dest):
    return base("expert/%s" % dest)

def fe_expert_client(client):
    return fe_expert("client/%s" % client)

def fe_user_pick():
    return base('pick-expert')

def full_url(rest):
    return "https://jonnyinc.herokuapp.com%s" % rest

def apply_for_job_url(job_id, user_id):
    return full_url(reverse('apply_for_job', args=(job_id, user_id,)))
