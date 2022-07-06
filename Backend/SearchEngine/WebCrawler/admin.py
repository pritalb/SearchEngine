from django.contrib import admin

from .models import Index, Url, CrawlFrontier, CrawledSites

# Register your models here.
admin.site.register(Index)
admin.site.register(Url)
admin.site.register(CrawledSites)
admin.site.register(CrawlFrontier)