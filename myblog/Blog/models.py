from django.db import models
class blog(models.Model):
	title=models.CharField(max_length=200, blank=True)
	text=models.TextField()
	slug=models.SlugField()
	date_added=models.DateTimeField(auto_now=True)
	class Meta:
		ordering=['-date_added']


# Create your models here.

