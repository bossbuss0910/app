from django.db import models

# Create your models here
'''
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
'''
class Gps(models.Model):
	u_id = models.IntegerField()
	name = models.CharField(max_length=30)
	latitude = models.DecimalField(max_digits=5, decimal_places=2)
	longitude = models.DecimalField(max_digits=5, decimal_places=2)

class Friend(models.Model):
	gps = models.ForeignKey(Gps)

