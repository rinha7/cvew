from django.db import models

# Create your models here.
# blog/models.py

from django.db import models

class Post(models.Model):
	photo = models.ImageField(blank=True,upload_to="images/raw")