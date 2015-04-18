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

  destination = forms.ChoiceField(choices=TARGETS)

  test = forms.BooleanField(required=False, initial=True)

  def google(self):
    return {
      'location': self.cleaned_data['location'],
      'keyword': self.cleaned_data['keyword'],
      'types': self.cleaned_data['types'],
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