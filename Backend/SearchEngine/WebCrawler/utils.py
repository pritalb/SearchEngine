# find substrings of a string which come after the start(type: str) and before the immediately next occurence of end(type: str)
def getSubstring(str, start, end):
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

def getURLs(html):
    return getSubstring(html, 'href="', '"')

def getKeywords(html):
    tags_to_consider_paired = ['title', 'body'] #tags that are used alongside their respective closing tags
    tags_to_consider_self_closing = ['img',]
    tags_to_consider_non_closing = ['meta',]
    info = {}

    # for robot meta tag
    nofollow = False
    noindex = False

    for tag in tags_to_consider_paired:
        info[tag] = getSubstring(html, f'<{tag}>', f'</{tag}>')

    return info