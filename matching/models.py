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


	