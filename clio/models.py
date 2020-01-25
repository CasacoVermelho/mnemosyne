from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Hangout(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateField()
	start = models.TimeField()
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name