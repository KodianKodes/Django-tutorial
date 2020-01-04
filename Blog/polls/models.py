from django.db import models

# Create your models here.
class News(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
