from django import forms

class GPSearchForm(forms.Form):
  TARGETS = (
    ('ReCa', 'ReCa'),
    ('Accomodation', 'Accomodation'),
    ('Activity', 'Activity'),
  )
  location = forms.CharField()
  keyword = forms.CharField()
  types = forms.MultipleChoiceField(required=False)

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
