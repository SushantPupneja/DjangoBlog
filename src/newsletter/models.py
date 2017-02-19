from django.db import models

# Create your models here.

class SignUp(models.Model):
	email		=	models.EmailField()
	full_name	=	models.CharField(blank=True, null=True, max_length=50)
	timestamp	=	models.DateTimeField(auto_now_add=True, auto_now=False)
	update		=	models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email

