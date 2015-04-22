from django.contrib import admin
from models import Agent, ReCa, Accomodation, Beach, Activity, Contact 

@admin.register(ReCa, Activity, Accomodation)
class VenueAdmin(admin.ModelAdmin):
  list_display = ('name', 'rating', 'description',)
  list_filter = ('rating',)
  search_fields = ['name', 'description', 'address']
  save_on_top = True

@admin.register(Beach)
class BeachAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'description',)
  list_filter = ('name',)


admin.site.register(Agent)
admin.site.register(Contact)


