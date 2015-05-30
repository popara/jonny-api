import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django_boto.s3.shortcuts import upload as UP
from rest_framework.parsers import MultiPartParser, FileUploadParser
from serializers import UploadResult

PRICE_IN_CENTS = 5000

import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

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
    THUMB_SIZE = 120, 120
    print request.data
    file = request.data['file']

    url = UP(file, prefix="experts")
    thumb = url
    data = UploadResult(data={"url":url, "thumb":thumb})
    data.is_valid()
    return Response(data.data)

charge = ChargeView.as_view()
upload = UploadImage.as_view()
