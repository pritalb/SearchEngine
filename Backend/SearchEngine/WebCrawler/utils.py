# find substrings of a string which come after the start(type: str) and before the immediately next occurence of end(type: str)
from string import punctuation


def getStringPart(str, start, end):
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
    escape_chars = ['\n', '\t']
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

    words_len = len(words)
    for substring_length in range(1, words_len + 1):
        current_index = 0
        end = substring_length + current_index

        while  end <= words_len:
            subs.append(' '.join(words[current_index : end]))
            current_index += 1
            end = substring_length + current_index

    return subs

def removeTags(html):
    page = html[:]

    while '<' in page:
        tag_starting = page.find('<')
        tag = page[tag_starting : page.find('>') + 1]

        page = page.replace(tag, '')

        closing_tag = page[page.find('</') : page.find('>') + 1]
        
        page = page.replace(closing_tag, '')
    return page


def getURLs(html):
    return getStringPart(html, 'href="', '"')

def getKeywords(html):
    tags_to_consider_paired = ['title', 'body'] #tags that are used alongside their respective closing tags
    # tags_to_consider_non_paired = ['meta',]
    metadata = getStringPart(html, f'<meta', '>')
    info = {}
    keywords = {}

    # for robot meta tag
    nofollow = False
    noindex = False

    for tag in tags_to_consider_paired:
        info[tag] = getStringPart(html, f'<{tag}>', f'</{tag}>')

    for tag in info.keys():
        for elem in info[tag]:
            keywords[tag] = getSubstrings(elem)
    
    # for tag in tags_to_consider_non_paired:
    #     info[tag] = getStringPart(html, f'<{tag}', '>')

    return keywords