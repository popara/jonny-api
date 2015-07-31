from rest_framework.views import APIView
from rest_framework.response import Response
from cache_model import get_next 

class RoundRobinView(APIView):
    def get(self, request):
        return Response(get_next())

round_robin = RoundRobinView.as_view()
