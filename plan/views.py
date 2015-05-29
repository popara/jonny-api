import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django_boto.s3 import upload
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser

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
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request):
    file = request.data['file']
    print "---------"
    print request
    print file
    print file.name
    name = upload(file, prefix="experts")
    print "nam"
    print name
    return Response(name)

charge = ChargeView.as_view()
upload = UploadImage.as_view()
