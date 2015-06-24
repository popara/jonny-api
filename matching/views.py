from . import tasks as t
from rest_framework.views import APIView
from rest_framework.response import Response
from firestone.models import job_queue_position_words, SOFT_LIMIT_PERIOD

class StartJobView(APIView):
    def post(self, request, job_id):
        c = (t.get_experts.s()
        | t.notify_experts.s(job_id)
        | t.start_hard_limit.si(job_id))

        c.delay()

        return Response(job_id)

class ApplyForJobView(APIView):
    def post(self, request, job_id, user_id):
        try:
            t.apply_for_job(user_id, job_id)
        except Exception as e:
            return Response(e.__str__(), status=401)

        t.start_soft_limit.delay(job_id, SOFT_LIMIT_PERIOD())
        return Response(job_queue_position_words(job_id))


start_job = StartJobView.as_view()
job_apply = ApplyForJobView.as_view()
