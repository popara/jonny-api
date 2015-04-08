from django.shortcuts import render
from django.views import generic 
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .forms import GPSearchForm
from .models import enquire_google_places

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
      (new_venues, dcs) = enquire_google_places(**f.enquiry())
      context.update({'result': new_venues, 'new_ammount': dcs.objects.count() })

    return render(request, "matching/scrap.html", context)


  @method_decorator(staff_member_required)
  def dispatch(self, request, *args, **kwargs):
      return super(PreScrap, self).dispatch(request, *args, **kwargs)


prescrap = PreScrap.as_view()

