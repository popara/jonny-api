from django.db import models


class Agent (models.Model):
  name = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  title = models.CharField(max_length=150)
  notes = models.TextField()
  website = models.URLField(max_length=200)
  company_phone = models.CharField(max_length=200)
  personal_phone = models.CharField(max_length=200)
  skype = models.CharField(max_length=50)
  whatsapp = models.CharField(max_length=50)
  email = models.EmailField(max_length=200)
  facebook_page = models.URLField(max_length=200)
  facebook_likes = models.IntegerField()
  facebook_posts = models.IntegerField()
  facebook_last_post = models.DateField(auto_now=False)
  twitter = models.URLField(max_length=200)
  twitter_tweets = models.IntegerField()
  twitter_followers = models.IntegerField()
  linkedin = models.URLField(max_length=200)
  fees = models.IntegerField()
  english = models.BooleanField(default=False)
  spanish = models.BooleanField(default=False)
  dutch = models.BooleanField(default=False)
  german = models.BooleanField(default=False)
  russian = models.BooleanField(default=False)
  french = models.BooleanField(default=False)
  italian = models.BooleanField(default=False)
  portuguese = models.BooleanField(default=False)
  arabic = models.BooleanField(default=False)
  SEO = models.CharField(max_length=10)
  SEM = models.CharField(max_length=10)
  hq = models.CharField(max_length=100)
  local_office = models.TextField()
  other_office = models.TextField()
  services = models.TextField()

  def __unicode__(self):
    return "%s - %s" % (self.name, self.company)

class Contact(models.Model):
  name = models.CharField(max_length=50)
  title = models.CharField(max_length=20, blank=True)
  phone = models.CharField(max_length=20, blank=True)
  email = models.EmailField(max_length=100, blank=True)

  fb = models.URLField(max_length=200, blank=True)
  twitter = models.URLField(max_length=200, blank=True)
  linkedin = models.URLField(max_length=200, blank=True)


  def __unicode__(self):
    return "%s" % self.name 

class WorkingHours(models.Model):
  mon = models.CharField(max_length=20, help_text="Monday")
  tue = models.CharField(max_length=20, help_text="Tuesday")
  wed = models.CharField(max_length=20, help_text="Wednesday")
  thu = models.CharField(max_length=20, help_text="Thursday")
  fri = models.CharField(max_length=20, help_text="Friday")
  sat = models.CharField(max_length=20, help_text="Saturday")
  sun = models.CharField(max_length=20, help_text="Sunday")

class Venue(models.Model):
  name = models.CharField(max_length=200)
  contacts = models.ManyToManyField(Contact, blank=True)
  address = models.CharField(max_length=200)
  type = models.CharField(max_length=10)
  description = models.TextField()
  website = models.URLField(max_length=150, blank=True)
  working_hours = models.ManyToManyField(WorkingHours)
  price_range = models.CharField(max_length=5, blank=True)
  rating = models.FloatField(default=0, blank=True)
  facebook = models.URLField(max_length=200, blank=True)
  facebook_likes = models.IntegerField(default=0, blank=True)
  facebook_acivity = models.CharField(max_length=200, blank=True)
  twitter = models.URLField(max_length=200, blank=True)
  twitter_followers = models.IntegerField(default=0, blank=True)
  twitter_tweets = models.IntegerField(default=0, blank=True)
  instagram = models.URLField(max_length=200, blank=True)
  instagram_followers = models.IntegerField(default=0, blank=True)
  
  beach = models.ForeignKey('Beach', related_name='venues', blank=True)

  def __unicode__(self):
    return "%s" % self.name 

class ReCa(Venue):
  type_of_venue = models.CharField(max_length=20)
  cousine_style = models.CharField(max_length=200)
  foods = models.TextField(blank=True)
  drinks = models.TextField(blank=True)

class Accomodation(Venue):
  rooms = models.IntegerField(default=1)
  bathrooms = models.IntegerField(default=1)
  beds = models.IntegerField(default=1)
  pool = models.BooleanField(default=False)
  airbnb = models.URLField(max_length=100)

class Activity(Venue):
  pass 

class Beach(models.Model):
  BEACH_TYPES = (
    ('sandy', 'Sandy'),
    ('rocky', 'Rocky'),
    ('concrete', 'Concrete'),
    ('misc', 'Mixed'),
  )

  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  type = models.CharField(max_length=10, choices=BEACH_TYPES)
  description = models.TextField()


  def __unicode__(self):
    return "%s" % self.name 