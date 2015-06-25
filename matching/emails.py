from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from . import strings as S

def email_template(to, from_, subject, template, context):
    template_txt = "%s.txt" % template
    template_html = "%s.html" % template

    text_c = render_to_string(template_txt, context)
    html_c = render_to_string(template_html, context)

    return send_mail(subject, text_c, from_, to, html_message=html_c)

def our_email_template(to, subject, template, context):
    return email_template(to, sender(), subject, template, context)


def sender():
    return 'mrwolf@jonnyibiza.com'


def job_start_expert(expert, details, link):
    return our_email_template([expert['email']], \
        S.expert_job_start_subject, \
        "matching/emails/expert_job_start", \
        dict(expert=expert, details=details, link=link)
     )

def job_done_client(client, link):
    return our_email_template([client['email']], \
        S.client_job_done, \
        "matching/emails/client_job_done", \
        dict(name=client['first_name'], link=link)
    )
