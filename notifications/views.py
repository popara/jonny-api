from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import TwilioRestClient

def get_twilio_client():
    return TwilioRestClient(account=settings.TWILIO_SID, token=settings.TWILIO_TOKEN)

def sender():
    return settings.TWILIO_DEFAULT_SENDER

def get_mrwolf_no():
    return settings.MR_WOLF_DEST_NO

def mrwolf_email():
    return settings.MR_WOLF_EMAIL

def mrwolf_email_dest():
    return settings.MR_WOLF_EMAIL_DEST

def fe(cat, link):
    return "https://www.jonnyibiza.com/%s/%s" % (cat, link)

def sms_to(number, text):
    client = get_twilio_client()
    number = get_mrwolf_no()
    from_no = sender()

    message = client.messages.create(body=text, to=number, from_=from_no)


e_from = "Mr. Wolf <%s>" % mrwolf_email()

class NotifyOnRegistration(APIView):
    def post(self, request):
        client_first_name = request.data["client_first_name"]
        client_name = request.data["client_name"]
        client_email = request.data["client_email"]

        # To Traveler
        link = client_email
        subject = "Welcome to Jonny Ibiza"
        body = "Hi %s \n\n You have successfully registered with jonnyibiza.com. \n\n"\
            "Your login is: %s \n\n Cheers from Ibiza! \n\n Jonny Ibiza" \
            % (client_first_name, link)

        send_mail(subject, body, e_from, [client_email])


        # To Mr. Wolf
        subject = "New traveler!"
        body = "Mr. Wolf - %s has just registered on jonnyibiza.com.  Click here to see the Traveler's details.  - The Jonny Ibiza Robot" \
            % (client_name)

        send_mail(subject, body, e_from, [mrwolf_email_dest()])

        return Response("ok")




class NotifyOnUserPurchase(APIView):
    def post(self, request):
        client = get_twilio_client()
        from_no = sender()

        client_first_name = request.data['client_first_name']
        client_name = request.data['client_name']
        client_email = request.data['client_email']
        client_id = request.data['client_id']
        expert_email = request.data['expert_email']
        expert_name = request.data['expert_name']
        phoneno = request.data['phoneno']
        time = request.data['time']

        # To Traveler

        chat_link_agent = fe("app", "chat/agent")

        subject = "We think you rock!"
        body = "Hi %s \n\n Thanks for ordering your Plan from Jonny Ibiza! \n\n" \
            "%s will get to work on it right away. \n\n"\
            "(S)He will have it to you no later than tomorrow @ %s. \n\n "\
            "In the meantime, you can feel free to chat with %s " \
            "if you want to provide him/her any additional information about you or your trip. \n\n %s \n\n" \
            "Cheers from Ibiza! \n\n Jonny Ibiza" \
            % (client_first_name, expert_name, time, expert_name, chat_link_agent)
        e_from = "Mr. Wolf <%s>" % mrwolf_email()

        send_mail(subject, body, e_from, [client_email])

        # To Mr. Wolf
        subject = "We have a payed customer!"
        body = "Mr. Wolf - FYI, %s has just paid(!) for a plan on jonnyibiza.com. The Jonny Ibiza Robot" \
            % (client_name)

        send_mail(subject, body, e_from, [mrwolf_email_dest()])

        link = fe("wolf", "user/%s" % client_id)
        text = "%s have bought a Plan! Link to his case: %s" % (client_name, link)
        sms_to(get_mrwolf_no(), link)

        # To Selected Jonny
        link = fe("expert", "client/%s" % client_id)
        chat_link_us = fe("expert", "chat/us")

        subject = "You are matched with a Traveler!"
        body = "Hi %s - Congrats! \n\n "\
            "You have a new Jonny Ibiza plan request.  \n\n"\
            "Your new Traveler is %s.  \n\n You have 18 hours to submit the Plan to %s. \n\n "\
            "Click here to prepare the plan for %s. \n\n %s \n\n" \
            "Click here %s if you have any problems or need any help from us. \n\n"\
            "Cheers! \n Jonny Ibiza" \
            % (expert_name, client_name, client_first_name, client_first_name, link, chat_link_us)

        send_mail(subject, body, e_from, [expert_email])


        text = "You have a new Jonny Ibiza plan request. \n\n Click here to prepare plan for %s. \n\n %s \n\n" \
            % (client_name, link)

        m = client.messages.create(body=text, to=phoneno, from_=from_no)

        return Response(m.status)


class NotifyPlanIsReady(APIView):
    def post(self, request):
        client_name = request.data['client_name']
        client_first_name = request.data['client_first_name']
        client_email = request.data['client_email']
        expert_name = request.data['expert_name']
        expert_email = request.data['expert_email']

        # To Traveler

        link = fe("app", "plan")
        chat_link_agent = fe("app", "chat/agent")
        chat_link_us = fe("app", "chat/us")
        subject = "Your Plan is ready!"
        body = "Hi %s, \n\n %s has completed your custom travel plan for Ibiza!  \n\n "\
            "Just click here to see it. %s  \n\n"\
            "You can chat with %s by clicking here. \n\n %s  \n\n "\
            "Or you can chat directly with us at Jonny Ibiza by clicking here. \n\n %s \n\n"\
            "We're sure you'll have an amazing trip.  \n\n"\
            "Let us know if we can help in any way. \n\n Cheers from Ibiza! - \n\n Jonny Ibiza" \
            % (client_name, expert_name, link, expert_name, chat_link_agent, chat_link_us)
        e_from = "Mr. Wolf <%s>" % mrwolf_email()

        send_mail(subject, body, e_from, [client_email])



        # To Expert
        chat_link_us = fe("expert", "chat/us")

        subject = "Mission Complete!"
        body = "Hi %s \n\n Congrats!  You've submitted a custom travel plan for %s. \n\n"\
            "Please remember to Click here if you have any problems or need any help from us. %s \n\n"\
            "Cheers! \n\n Jonny Ibiza" \
            % (expert_name, client_name, chat_link_us)

        send_mail(subject, body, e_from, [expert_email])



        return Response("ok")


class NotifyWolfView(APIView):
    def post(self, request):
        client = get_twilio_client()
        number = get_mrwolf_no()
        from_no = sender()

        user_name = request.data["user_name"]
        user_id = request.data["user_id"]
        snipp = request.data["snipp"]

        link = fe("wolf", "/chat/user/%s" % user_id)
        text = "Mr. Wolf, you have a new chat from %s, Click here to reply: %s" \
            % (user_name, link)


        message = client.messages.create(body=text, to=number, from_=from_no)

        subject = "Mr Wolf, new chat message"
        send_mail(subject, text, e_from, [mrwolf_email_dest()])

        return Response(message.status)


class NotifyOnExpertChat(APIView):
    def post(self, request):
        expert_name  = request.data["expert_name"]
        client_id  = request.data["client_id"]
        client_name  = request.data["client_name"]
        client_email  = request.data["client_email"]
        snipp = request.data["snipp"]


        # To Traveler

        link = fe("app", "plan")
        chat_link_agent = fe("app", "chat/agent")
        chat_link_us = fe("app", "chat/us")
        subject = "You have a new chat message!"
        body = "You have a new chat message from your Jonny, %s!  \n\n "\
            "Just click here to see it. \n\n %s  \n\n"\
            % (expert_name, chat_link_agent)
        e_from = "Mr. Wolf <%s>" % mrwolf_email()

        send_mail(subject, body, e_from, [client_email])


        # To Mr. Wolf
        link = fe("wolf", "chat/%s" % client_id)
        subject = "Jonny Sent a Message"
        body = "Mr. Wolf \n\n %s has just sent a message to %s.  This is the message: %s.  Click here to see message thread. %s" \
            % (expert_name, client_name, snipp, link)
        e_from = "Mr. Wolf <%s>" % mrwolf_email()
        send_mail(subject, body, e_from, [mrwolf_email_dest()])


        return Response("ok")

class NotifyOnClientChat(APIView):
    def post(self, request):
        client = get_twilio_client()
        from_no = sender()

        client_id  = request.data["client_id"]
        client_name  = request.data["client_name"]
        client_first_name = request.data['client_first_name']
        expert_name  = request.data["expert_name"]
        expert_phone = request.data["expert_phone"]
        snipp = request.data["snipp"]


        # To Mr. Wolf

        link = fe("wolf", "chat/%s" % client_id)

        subject = "Chat activity: %s" % client_name
        body = "Mr. Wolf, \n\n %s, has just sent a message to %s.  This is the message: %s.  Click here to see message thread. %s" \
            % (client_name, expert_name, snipp, link)
        e_from = "Mr. Wolf <%s>" % mrwolf_email()

        send_mail(subject, body, e_from, [mrwolf_email_dest()])

        # To Expert

        link = fe("expert", "chat/user/%s" % client_id)
        body = "%s, you have a new chat from %s.  Click here to reply: %s" \
            % (expert_name, client_name, link)

        message = client.messages.create(body=body, to=expert_phone, from_=from_no)

        return Response(message.to)


registered = NotifyOnRegistration.as_view()
got_plan = NotifyOnUserPurchase.as_view()
plan_ready = NotifyPlanIsReady.as_view()

wolf_chat = NotifyWolfView.as_view()
jonny_chat = NotifyOnExpertChat.as_view()
user_chat = NotifyOnClientChat.as_view()
