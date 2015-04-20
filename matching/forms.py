from django import forms

from googleplaces import types

class GPSearchForm(forms.Form):
  TARGETS = (
    ('ReCa', 'ReCa'),
    ('Accomodation', 'Accomodation'),
    ('Activity', 'Activity'),
  )
  TYPES_LIST = list((getattr(types, t)) for t in dir(types) if t.startswith("TYPE"))
  TYPES = map(lambda t: (t, t), TYPES_LIST)

  location = forms.CharField()
  keyword = forms.CharField()
  types = forms.MultipleChoiceField(required=False, choices=TYPES)

  lat = forms.FloatField(initial=39.007612)
  lng = forms.FloatField(initial=1.443494)
  radius = forms.FloatField(initial=3500)
  destination = forms.ChoiceField(choices=TARGETS)

  test = forms.BooleanField(required=False, initial=True)

  def google(self):
    return {
      'location': self.cleaned_data['location'],
      'keyword': self.cleaned_data['keyword'],
      'types': self.cleaned_data['types'],
      'lat_lng': {
        'lat': self.cleaned_data['lat'],
        'lng': self.cleaned_data['lng'],
      },
      'radius': self.cleaned_data['radius'],
    }

  def dest(self):
    return self.cleaned_data['destination']

  def just_test(self):
    return self.cleaned_data['test']

  def enquiry(self):
    return {
      'google': self.google(),
      'dest': self.dest(),
      'test': self.just_test(),
    }