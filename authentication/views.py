from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(APIView):
  def post(self, request):
    return Response(status=status.HTTP_200_OK)

register = RegisterView.as_view()