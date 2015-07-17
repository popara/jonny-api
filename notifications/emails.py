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

def user_registration(name, email, pwd, link):
    return our_email_template([email], \
        S.client_register_subject, \
        "notifications/emails/reg", \
        dict(name=name, email=email, pwd=pwd, link=link, mrwolf=sender()), \
    )
