from utils import getURLs, getKeywords, getSubstrings

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
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Id, eveniet. Obcaecati,
            esse illo deleniti fugiat molestiae mollitia adipisci qui ab, neque quos, natus
            quis exercitationem in. Dolore non aut quo?
        </p>
    </body>
    </html>
'''

# print(getURLs(html))
# print(getKeywords(html))
# string = "The whole secret of a successful life is to find out what is one’s destiny to do, and then do it. - Henry Ford"
string = 'This is a sample sentence.'
print(getSubstrings(string))