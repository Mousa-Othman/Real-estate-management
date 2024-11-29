from django.db import models
from datetime import datetime


# Create your models here.

class Realtor(models.Model):
	name     	= models.CharField(max_length = 100)
	phone   	= models.CharField(max_length = 32)
	email   	= models.CharField(max_length = 50)
	address   	= models.CharField(max_length = 200)
	description	= models.TextField(blank = True)
	profile_img = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
	is_mvp		= models.BooleanField(default = True)
	hire_date   = models.DateTimeField(default = datetime.now, blank = True)

	def __str__(self):
		return self.name
	  

		