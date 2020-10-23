from django.db import models

# Create your models here.
# blog/models.py

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	photo = models.ImageField(blank=True)