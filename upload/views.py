from rest_framework.views import APIView
from rest_framework.response import Response
from django_boto.s3.shortcuts import upload as UP
from rest_framework.parsers import FileUploadParser
from serializers import UploadResult

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


upload = UploadImage.as_view()
