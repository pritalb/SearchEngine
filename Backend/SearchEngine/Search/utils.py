# from  django.apps import apps

# Index = apps.get_model('WebCrawler', 'Index')
from WebCrawler.models import Index

def rank(index_objects):
    result_urls = {}
    ranked_results = {}

    for index_object in index_objects:
        url_objects = index_object.urls.all()

        for url_object in url_objects:
            url = url_object.url

            if url in result_urls.keys():
                result_urls[url]['keyword_count'] += 1
            else:
                result_urls[url] = {
                    'title' : url_object.title,
                    'backlinks': url_object.backlinks,
                    'keyword_count' : 1,
                }

    for url in result_urls.keys():
        url_info = result_urls[url]
        url_score = url_info['backlinks'] + url_info['keyword_count']


        ranked_results[url_score] = {
            'url': url,
            'title': url_info['title'],
            'ranking_score': url_score,
            'backlinks': url_info['backlinks'],
            'keywords_present': url_info['keyword_count'],
        }

    return ranked_results

def search(keywords):
    raw_queries = [] # a list of Index model objects, not the urls!

    for keyword in keywords:
        keyword_results = Index.objects.filter(keyword=keyword)
        raw_queries = raw_queries + list(keyword_results)

    ranked_results = rank(raw_queries)
    return ranked_results