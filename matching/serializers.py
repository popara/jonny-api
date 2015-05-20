from rest_framework.serializers import ModelSerializer
from .models import ReCa, Activity, Accomodation, Beach


class VenueSerializer(ModelSerializer):

  class Meta:
    exclude = ('internal_notes', 'internal_rating')


class ReCaSerializer(VenueSerializer):
  class Meta:
    model = ReCa



class ActivitySerializer(ModelSerializer):
  class Meta:
    model = Activity


class AccomodationSerializer(ModelSerializer):
  class Meta:
    model = Accomodation


class BeachSerializer(ModelSerializer):
  class Meta:
      model = Beach
