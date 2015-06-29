from funcy import compose, partial, walk, mapcat, first,\
    str_join
from firestone import get_user, get_f, merge_id
from django.core.urlresolvers import reverse
import date_converter


w_ids = partial(walk, lambda (k, v): merge_id(k, v))
as_arr = partial(lambda v: v.values())
mids = compose(as_arr, w_ids)

p_collection = compose(as_arr, w_ids)
extract_qs = partial(map, lambda a: a['questions'])


class JobStatus:
    drafting = "drafting"
    drafted = "drafted"
    selected = "selected"


def job_status(job):
    return job['status']


def user_selected(job, user_id):
    return (job['status'] is JobStatus.selected) and \
        (get_user(job['owner'])['expert'] == user_id)


def picked_expert(job):
    return 'expert' in get_user(job['owner'])


def job_applied_status(job, user_id):

    still_in_progress = (job_status(job) == JobStatus.drafting)
    selected = not still_in_progress and \
        (user_selected(job, user_id))
    done_not_selected = not still_in_progress and not selected
    done_selected = selected
    idle = not still_in_progress and not picked_expert(job)

    return {
        'in_progress': still_in_progress,
        'done_selected': done_selected,
        'done_not_selected': done_not_selected,
        'idle': idle
    }


def base(rest):
    return "https://jonnyibiza.com/%s" % rest


def fe_expert(dest):
    return base("expert/%s" % dest)


def fe_expert_client(client):
    return fe_expert("client/%s" % client)


def fe_user_pick():
    return base('app/pick-expert')


def full_url(rest):
    return "https://jonnyinc.herokuapp.com%s" % rest


def apply_for_job_url(job_id, user_id):
    return full_url(reverse('apply_for_job', args=(job_id, user_id,)))


def get_details(user_id):
    return zipthem(get_questions(), get_answers(user_id))


def zipthem(questions, answers):
    def id(a): return a['id']
    def ty(a): return a['type']
    def txt(a): return a['text']
    def v(a): return a['value']

    def q_with_id(qid):
        return first(filter(lambda q: id(q) == qid, questions))

    def q_for_ans(ans):
        q = q_with_id(id(ans))
        return {
            'answer_str': answer_as_str(v(ans), ty(q)),
            'question': txt(q),
            'answer': ans,
        }


    return map(q_for_ans, answers)


def get_answers(user_id):
    return get_anons_answers(get_anon(user_id))

def get_anon(user_id):
    return get_user(user_id)['anon']

def get_anons_answers(anon_id):
    a = get_f('answers')(anon_id)
    if a is not None:
        return mids(a)
    else:
        return []


def get_questions():
    ls = p_collection(get_f('levels')())
    qs = extract_qs(ls)

    def a(lq):
        return mids(lq)

    return mapcat(a, qs)


def answer_as_str(answer, qtype):
    def j(v): return str_join(', ', v)

    if qtype == 'check-list':
        return j(answer)
    elif qtype == 'bingo':
        return j(answer)
    elif qtype == 'about':
        return j(answer.values())
    elif qtype == 'company-details':
        return j(about_company(answer))
    elif qtype == 'dates':
        return j(dates_answer(answer))
    elif qtype == 'rolling':
        return budget_names(answer)

    return answer.__str__()


def about_company(cd):
    r = []
    r += ['With partner'] if 'partner' in cd and cd['partner'] else ''

    if 'malefriends' in cd:
        r += ['Male friends: %s' % cd['malefriends']['count']]

    if 'femalefriends' in cd:
        r += ['Female friends: %s' % cd['femalefriends']['count']]

    if 'kids' in cd:
        a = ['Kids:']
        a += ['%s Boys' % cd['kids']['boys']] if 'boys' in cd['kids'] else []
        a += ['%s Girls' % cd['kids']['girls']] if 'girls' in cd['kids'] else []

        r += [str_join(' ', a)]

    r += [cd['details']]

    return r


def dates_answer(dates):
    date_format = '%B %d, %Y'
    d = []

    if 'start' in dates:
        start = sanitize_date(dates['start'])
        d += ['From %s' % date_converter.timestamp_to_string(start, date_format)]

    if 'end' in dates:
        end = sanitize_date(dates['end'])
        d += ['To %s' % date_converter.timestamp_to_string(end, date_format)]

    if 'flexible' in dates:
        if dates['flexible']:
            d += ["Dates are flexible!"]

    return d


def sanitize_date(date):
    return int(date)/1000


def budget_names(val):
    if val == 1:
        return 'Backpacker'
    elif val == 2:
        return 'Cosmopolitan'
    elif val == 3:
        return 'Jetsetter'
    elif val == 4:
        return 'Rock star!'
    elif val == 5:
        return 'MOTHERFUCKING SULTAN!'
