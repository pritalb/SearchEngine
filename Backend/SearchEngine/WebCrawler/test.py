from ast import keyword
from urllib import response
import requests
from utils import test_webCrawler, getMultipleStringParts, getDomain

endpoint = 'https://sites.s3.jp-tok.cloud-object-storage.appdomain.cloud/noindex.html'
# response = requests.get(endpoint)
# html = response.text

# print(getDomain('http://www.site.com/some/route'))
test_webCrawler()