import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django_boto.s3.shortcuts import upload as UP
from rest_framework.parsers import MultiPartParser, FileUploadParser

from django.views.generic import View
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse as render

PRICE_IN_CENTS = 5000

class ChargeView(APIView):
  def post(self, request):
    stripe.api_key = settings.STRIPE_API_KEY
    token = request.data['token']
    amount = PRICE_IN_CENTS
    currency = "eur"
    desc = "Charging for a plan"
    try:
      charge = stripe.Charge.create(
        amount=amount,
        currency=currency,
        source=token,
        description=desc,
      )
      return Response(status.HTTP_200_OK)
    except (stripe.CardError, stripe.InvalidRequestError) as e:
      return Response(str(e), status.HTTP_406_NOT_ACCEPTABLE)


  def get(self, request):
    return Response(":)")


class UploadImage(APIView):
  parser_classes = (FileUploadParser,)
  def post(self, request):
    name =  request.data['name']
    print request.data
    x = request.FILES['file']
    name = UP(x, name=name, prefix="experts")
    print "-done -- "
    print name
    return render(name)

    
@ensure_csrf_cookie
def csrf(request):
  return render(get_token(request))

charge = ChargeView.as_view()
upload = UploadImage.as_view()
