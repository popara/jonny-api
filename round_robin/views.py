from rest_framework.views import APIView
from rest_framework.response import Response
from models import get_next

class RoundRobinView(APIView):
    def get(self, request, robin_id):
        return Response(get_next(robin_id))

round_robin = RoundRobinView.as_view()
