# find substrings of a string which come after the start(type: str) and before the immediately next occurence of end(type: str)
from msilib.schema import Directory
from string import punctuation
import requests


# sample data structures
# to be replaced by models once they work

crawl_frontier = ['https://sites.s3.jp-tok.cloud-object-storage.appdomain.cloud/seed.html',]
crawled_sites = []
index = {}
site_directory = {}

#

def getStringPart(str, start, end):
    str_copy = str

    start_len = len(start)
    next_start_position = str_copy.find(start)

    end_index = str_copy.find(end, next_start_position + start_len)
    res = str_copy[next_start_position + start_len : end_index] 

    return res

def getMultipleStringParts(str, start, end):
    res = []
    str_copy = str

    start_len = len(start)
    next_start_position = str_copy.find(start)

    while next_start_position != -1:
        end_index = str_copy.find(end, next_start_position + start_len)
        temp_res = str_copy[next_start_position + start_len : end_index] 

        res.append(temp_res)
        str_copy = str_copy[end_index : ]
        next_start_position = str_copy.find(start)
    return res

def getSubstrings(str):
    punctuation = ',.<>;:|()*^%$#@!`~/?[]{}\\-+=\" '
    escape_chars = ['\n', '\t', '\r']
    subs = []
    str_copy = str[:]
    sep = '&&sep&&'

    str_copy = str_copy.replace('&', ' and ')
    for escape_char in escape_chars:
        str_copy = str_copy.replace(escape_char, sep)

    for mark in punctuation:    
        str_copy = str_copy.replace(mark, sep)
    words = str_copy.split(sep)
    words = list(filter(lambda x: x != '', words))

    # the code below returns a list of substrings all all lenghts/sizes i.e. from 1 word substrings to a substring with all words
    # kept for future reference

    # words_len = len(words)
    # for substring_length in range(1, words_len + 1):
    #     current_index = 0
    #     end = substring_length + current_index

    #     while  end <= words_len:
    #         subs.append(' '.join(words[current_index : end]))
    #         current_index += 1
    #         end = substring_length + current_index

    # return subs
    return words

def removeTags(html):
    page = html[:]

    while '<' in page:
        tag_starting = page.find('<')
        tag = page[tag_starting : page.find('>') + 1]

        page = page.replace(tag, '')

        closing_tag = page[page.find('</') : page.find('>') + 1]
        
        page = page.replace(closing_tag, '')
    return page

def getDomain(url):
    domain_start = url.find('://') + 3
    domain_end = url.find('/', domain_start)

    return url[domain_start : domain_end]

def getURLs(html):
    return getMultipleStringParts(html, 'href="', '"')

def getKeywords(html):
    tags_to_consider_paired = ['title', 'body'] #tags that are used alongside their respective closing tags
    # tags_to_consider_non_paired = ['meta',]
    info = {}
    keywords = {}

    # for robot meta tag
    nofollow = False
    noindex = False

    for tag in tags_to_consider_paired:
        if tag in html:
            info[tag] = removeTags(getStringPart(html, f'<{tag}>', f'</{tag}>'))

    # print(info)
    # print('\n\n')
    for tag in info.keys():
        keywords[tag] = getSubstrings(info[tag])

    return keywords

def crawl(url):
    response = requests.get(url)
    html = response.text
    metadata = getMultipleStringParts(html, f'<meta', '>')
    robot_tag = ''

    for data in metadata:
        if ('name="robots"' in data) or ("name='robots'" in data):
            robot_tag = data
            break
    nofollow = 'nofollow' in robot_tag
    noindex = 'noindex' in robot_tag

    follow_urls = getURLs(html)
    keywords = getKeywords(html)

    # add data to db or update
    crawl_frontier.remove(url)


    if not nofollow:
        for follow_url in follow_urls:
            crawl_frontier.append(follow_url)
    
    if url not in crawled_sites:
        crawled_sites.append(url)

    if not noindex:
        for keyword in keywords['body']:
            if keyword in index.keys():
                related_sites = index[keyword]
                if not url in related_sites:
                    index[keyword].append(url)
            else:
                index[keyword] = [url]

        site_directory[url] = {
            'backlinks': 1,
            'title_keywords': keywords['title'], 
            'body_keywords': keywords['body'], 
            'normalized_url': getDomain(url),
            'domain': getDomain(url),
            'last_modified': response.headers['Last-Modified'],
        }
    # done adding data to db

def webCrawler():
    depth = 4
    current_depth = 0

    while current_depth < depth:
        sites_to_crawl = crawl_frontier[:]
        for url in sites_to_crawl:
            if not url in site_directory.keys():
                crawl(url)
            else:
                site_directory[url]['backlinks'] += 1
        current_depth += 1

def test_webCrawler():
    webCrawler()

    print(f'crawl frontier: {crawl_frontier} \n\n')
    print(f'crawled sites: {crawled_sites} \n\n')
    print(f'site directory: {site_directory} \n\n')
    print(f'index: {index} \n\n')