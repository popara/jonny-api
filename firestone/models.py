from . import get_job, APPLICANTS_KEY

class JobApplication:
    def __init__(self, user_id, at):
        self.user_id = user_id
        self.applied = at


class JobJob:
    def __init__(self, owner):
        self.owner = owner
        self.applicants = []


def job_queue_position(job_id):
    j = get_job(job_id)
    return len(j[APPLICANTS_KEY])

def job_queue_position_words(job_id):
    return position_word(job_queue_position(job_id))

def position_word(post):
    if post == 1:
        return 'first'
    elif post == 2:
        return 'second'
    elif post == 3:
        return 'third'
    elif post == 4:
        return 'fourth'
