from django.shortcuts import render
from django.views import generic 
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .forms import GPSearchForm
from .models import Venue
from . import models as Source
from googleplaces import GooglePlaces, types, lang

class PreScrap(generic.View):
  def get(self, request, *args): 
    return render(request, "matching/scrap.html", {
      'search': GPSearchForm()
      })

  def post(self, request): 
    f = GPSearchForm(request.POST)
    context = {
      'search' : f, 
    }

    if f.is_valid():
      gp = GooglePlaces('AIzaSyDU9pKdSl-G-ZDkrWeQe69dJqk5xRV0mgs')
      qr = gp.nearby_search(**f.google())
      places = qr.places 

      ids = map(lambda p: p.place_id, places)
      destination_cls = getattr(Source, f.dest())
      dcs = destination_cls

      existing_venues = dcs.objects.filter(google_place_id__in=ids)
      existing_venue_ids = map(lambda v: v.google_place_id, existing_venues)

      new_places = filter(lambda p: p.place_id not in existing_venue_ids, places)
      for p in new_places:
        p.get_details()  

      new_venues = map(lambda p: dcs.from_google_place(p), new_places)

      if not f.just_test():
        for v in new_venues:
          v.save()

      context.update({'result': new_venues, 'new_ammount': dcs.objects.count() })

    return render(request, "matching/scrap.html", context)


  @method_decorator(staff_member_required)
  def dispatch(self, request, *args, **kwargs):
      return super(PreScrap, self).dispatch(request, *args, **kwargs)


prescrap = PreScrap.as_view()

