from utils import getURLs, getKeywords, getSubstrings, removeTags

html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>A Very nice title</title>
    </head>
    <body>
        <a href="url_1"> Link_1 </a>
        <a href="url_2"> Link_2 </a>
        <a href="url_3"> Link_3 </a>

        <p>
            This is some good website content.
        </p>
    </body>
    </html>
'''

# html = '''
#     <body>
#         <a href="url_1"> Link_1 </a>
#         <a href="url_2"> Link_2 </a>
#         <a href="url_3"> Link_3 </a>

#         <p>
#             This is some good website content.
#         </p>
#     </body>
# '''

# print(getURLs(html))
print(removeTags(html))
# string = "The whole secret of a successful life is to find out what is one’s destiny to do, and then do it. - Henry Ford"
# string = 'This is a sample sentence.'
# print(getSubstrings(string))