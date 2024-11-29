from django.db import models
from listings.models import Listing
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
	listing = models.ForeignKey(Listing, on_delete= models.DO_NOTHING)
	user = models.ForeignKey(User, on_delete= models.DO_NOTHING)

	def __str__(self):
		return self.listing.title + ' ( ' + self.user.username + ' : ' + self.user.first_name + ' ' + self.user.last_name + ' ) '  