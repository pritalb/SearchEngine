from django import urls
from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField()
    title = models.TextField()
    last_updated = models.DateTimeField()
    backlinks = models.IntegerField()

class Index(models.Model):
    keyword = models.TextField(verbose_name='keyword')
    urls = models.ManyToManyField('Url', related_name='keywords' ,symmetrical=False)

class CrawlFrontier(models.Model):
    url =models.URLField()

class CrawledSites(models.Model):
    url = models.URLField()