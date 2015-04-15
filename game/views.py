from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class LevelView(APIView):
  pass


class AnswerView(APIView):
  pass

level = LevelView.as_view()
answer = AnswerView.as_view()

