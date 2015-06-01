from rest_framework import serializers

class UploadResult(serializers.Serializer):
    url = serializers.URLField()
    thumb = serializers.URLField()
