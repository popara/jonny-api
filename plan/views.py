import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class ChargeView(APIView):
  def post(self, request):
    stripe.api_key = settings.STRIPE_API_KEY
    token = request.data['token']
    amount = 1000
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


charge = ChargeView.as_view()