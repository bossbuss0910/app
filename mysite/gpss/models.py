from django.db import models

# Create your models here.
class Gps(models.Model):
	u_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	latitude = models.DecimalField(max_digits=5, decimal_places=2)
	longitude = models.DecimalField(max_digits=5, decimal_places=2)
	def __unicode__(self):
		return self.name

class Friend(models.Model):
	id = models.IntegerField(primary_key=True)
	user1id = models.IntegerField()
	user2id = models.IntegerField()

from django.contrib import admin
admin.site.register(Gps)
admin.site.register(Friend)
