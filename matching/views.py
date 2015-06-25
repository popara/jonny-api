from . import tasks as t
from django.shortcuts import render
from django.views.generic import TemplateView
from funcy import merge
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import job_applied_status, fe_expert_client
from firestone import get_user
from firestone.models import job_queue_position, SOFT_LIMIT_PERIOD,\
    has_space, get_job, position_word, job_drafting, has_applied, \
    order_word

class StartJobView(APIView):
    def post(self, request, job_id):
        if not job_drafting(job_id):
            c = (t.get_experts.s()
            | t.notify_experts.s(job_id)
            | t.start_drafting.si(job_id)
            | t.start_hard_limit.si(job_id))

            c.delay()

        return Response(job_id)

class ApplyForJobView(TemplateView):
    template_success = "matching/success.html"
    template_full = "matching/full.html"
    template_already = "matching/already.html"

    def post(self, request, job_id, user_id):
        job = get_job(job_id)
        expert = get_user(user_id)
        name = {'name': expert['first_name']}

        if has_applied(job, user_id):
            poz = {'order': order_word(job_queue_position(job))}
            link = {'link': fe_expert_client(job['owner'])}
            status = job_applied_status(job, user_id)
            context = merge(poz, status, link, name)
            return render(request, self.template_already, context)

        if has_space(job):
            job = t.apply_for_job(user_id, job, job_id)
            t.start_soft_limit.delay(job_id, SOFT_LIMIT_PERIOD())
            poz = job_queue_position(job)
            pos_word = position_word(poz)
            order_name = order_word(poz)
            c = {'position':pos_word,'order': order_word}
            context = merge(c, name)
            return render(request, self.template_success, context)

        return render(request, self.template_full, name, status=500)

start_job = StartJobView.as_view()
job_apply = ApplyForJobView.as_view()
