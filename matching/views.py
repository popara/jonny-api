from . import tasks as t
from rest_framework.views import APIView
from rest_framework.response import Response
from firestone.models import job_queue_position, SOFT_LIMIT_PERIOD,\
    has_space, get_job, position_word, job_drafting, has_applied

class StartJobView(APIView):
    def post(self, request, job_id):
        if not job_drafting(job_id):
            c = (t.get_experts.s()
            | t.notify_experts.s(job_id)
            | t.start_drafting.si(job_id)
            | t.start_hard_limit.si(job_id))

            c.delay()

        return Response(job_id)

class ApplyForJobView(APIView):
    def post(self, request, job_id, user_id):
        job = get_job(job_id)

        if has_applied(job, user_id):
            return Response("already")

        if has_space(job):
            job = t.apply_for_job(user_id, job, job_id)
            t.start_soft_limit.delay(job_id, SOFT_LIMIT_PERIOD())
            return Response(position_word(job_queue_position(job)))

        return Response("Full", status=500)

start_job = StartJobView.as_view()
job_apply = ApplyForJobView.as_view()
