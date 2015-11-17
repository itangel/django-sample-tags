from django.db import models

from taggit.managers import TaggableManager


class Book(models.Model):
	title = models.CharField(max_length=100)
	tags = TaggableManager()

