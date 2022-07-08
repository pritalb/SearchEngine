from django import urls
from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField()
    title = models.TextField()
    backlinks = models.IntegerField()

    def __str__(self):
        return self.title

class Index(models.Model):
    keyword = models.TextField(verbose_name='keyword')
    urls = models.ManyToManyField('Url', related_name='keywords' ,symmetrical=False)

    def __str__(self):
        return self.keyword

class CrawlFrontier(models.Model):
    url =models.URLField()

    def __str__(self):
        return self.url

class CrawledSites(models.Model):
    url = models.URLField()
    
    def __str__(self):
        return self.url