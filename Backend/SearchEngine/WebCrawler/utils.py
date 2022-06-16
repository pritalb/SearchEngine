def getURLs(html):
    urls = []
    page = html

    href = 'href="'
    href_len = len(href)
    next_href_position = page.find(href)

    while next_href_position != -1:
        url_end = page.find('"', next_href_position + href_len)
        url = page[next_href_position + href_len : url_end] 

        urls.append(url)
        page = page[url_end : ]
        next_href_position = page.find(href)
    return urls

def getKeywords(html):
    pass