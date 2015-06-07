from fixures import *
from django.core import mail
from django.conf import settings

CLIENT_NAME = "Joe"
CLIENT_EMAIL = "joe@doe.com"
EXPERT_NAME = "Miguel"
EXPERT_EMAIL = "miguel@hoe.com"
MR_WOLF_EMAIL = "mrwolf@jonnyibiza.com"
MR_WOLF_EMAIL_DEST = "support@jonnyibiza.com"
EXPERT_PHONE_NO = "+15005550012"
CLIENT_ID = "simleid:1"

TEST_SID = "ACad0296f1fbf1bbd4901a869f13382f0f"
TEST_TOKEN = "f642e0a9da05a2cc1f6a7de4a88036ee"
TEST_NO = "+15005550006"
TEST_DEST_NO = "+15005550012"

def test_user_registered(api, ok):
    # client_name
    r = api.post("/api/notifications/user_registered", {
        "client_name": CLIENT_NAME,
        "client_first_name": CLIENT_NAME,
        "client_email": CLIENT_EMAIL,
    })

    assert r.status_code == ok

    m1, m2  = mail.outbox

    assert m1.to == [CLIENT_EMAIL]
    assert m2.to == [MR_WOLF_EMAIL_DEST]


def test_user_charged(api, ok):
    # Email and SMS  to expert
    # Email to us
    # phoneno, email, client.name, client.id
    # To: traveler, Wolf, Expert


    s = settings

    s.TWILIO_SID = TEST_SID
    s.TWILIO_TOKEN = TEST_TOKEN
    s.TWILIO_DEFAULT_SENDER = TEST_NO

    r = api.post("/api/notifications/user_charged", {
        "client_name": CLIENT_NAME,
        "client_first_name": CLIENT_NAME,
        "client_email": CLIENT_EMAIL,
        "client_id": CLIENT_ID,
        "phoneno": EXPERT_PHONE_NO,
        "expert_name": EXPERT_NAME,
        "expert_email": EXPERT_EMAIL,
        "time": "noon"
    })
    m1, m2, m3 = mail.outbox

    assert m1.to == [CLIENT_EMAIL]
    assert m2.to == [MR_WOLF_EMAIL_DEST]
    assert m3.to == [EXPERT_EMAIL]

    assert r.status_code == ok
    assert r.data == 'queued'


def test_plan_ready(api, ok):
    # email client that plan is ready
    # client.email, client.name, expert.name,
    # To: Traveler, Expert

    r = api.post("/api/notifications/plan_ready", {
        "client_email": CLIENT_EMAIL,
        "client_name": CLIENT_NAME,
        "client_first_name": CLIENT_NAME,
        "expert_name": EXPERT_NAME,
        "expert_email": EXPERT_EMAIL,
    })

    m1, m2 = mail.outbox

    assert r.status_code == ok
    assert m1.to == [CLIENT_EMAIL]
    assert m2.to == [EXPERT_EMAIL]


def test_wolf_contacted(api, ok):
    # Sms to Wolf
    # user.name, user.id snipp

    s = settings

    s.TWILIO_SID = TEST_SID
    s.TWILIO_TOKEN = TEST_TOKEN
    s.TWILIO_DEFAULT_SENDER = TEST_NO

    SNIPP = "Hello, I just wanted to ask ..."

    r = api.post("/api/notifications/wolf_chat", {
        "user_name": CLIENT_NAME,
        "user_id": CLIENT_ID,
        "snipp": SNIPP,
    })

    m1 = mail.outbox[0]
    assert m1.to == [MR_WOLF_EMAIL_DEST]
    assert r.status_code == ok
    assert r.data != "failed"



def test_jonny_chat(api, ok):
    # to wolf
    SNIPP = "Jonny I miss you"
    r = api.post("/api/notifications/jonny_chat", {
        "client_name": CLIENT_NAME,
        "client_email": CLIENT_EMAIL,
        "client_id": CLIENT_ID,
        "expert_name": EXPERT_NAME,
        "snipp": SNIPP,
    })

    m1, m2 = mail.outbox

    assert m1.to == [CLIENT_EMAIL]
    assert m2.to == [MR_WOLF_EMAIL_DEST]
    assert r.status_code == ok



def test_user_chat(api, ok):

    # to jonny, wolf

    snipp = "Jonny I don't miss you"

    r = api.post("/api/notifications/user_chat", {
        "client_id": CLIENT_ID,
        "client_name": CLIENT_NAME,
        "client_first_name": CLIENT_NAME,
        "expert_name": EXPERT_NAME,
        "expert_phone": EXPERT_PHONE_NO,
        "snipp": snipp,
    })

    m1 = mail.outbox[0]

    assert m1.to == [MR_WOLF_EMAIL_DEST]
    assert r.status_code == ok

    assert r.data == EXPERT_PHONE_NO
