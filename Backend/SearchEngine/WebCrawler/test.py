from ast import keyword
from urllib import response
import requests
from utils import getURLs, getKeywords, getSubstrings, removeTags,getStringPart, crawl

endpoint = 'https://sites.s3.jp-tok.cloud-object-storage.appdomain.cloud/seed.html'
# response = requests.get(endpoint)
# html = response.text

print(crawl(endpoint), end='\n')