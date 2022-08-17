# SearchEngine
A basic Search Engine made using Django and ReactJs.

# Features
The Web Crawler respects robot meta tags.
Search Engine provides ranked results.

# Setup instructions
1. Navigate to the 'Backend' directory. This directory contains all our backend code.
2. Either start up the virtual env by entering ```  ./venv/Scripts/Activate.ps1  ``` into the terminal or create your own. Don't forget to install all the required packages in your virtual environment if you decide to create a new one.
    In case you get an "UnauthorizedAccess" error while trying to run your virtual env, you may need to give the terminal permission to run scripts with the help of the command:
    ```
    Set-ExecutionPolicy Unrestricted -Scope Process
    ```
3. Navigate to the 'SearchEngine' directory which contains our Django project code.
4. To connect Django to PostgreSQL, you will need to get your database credentials. Once you get your credentials, open 'SearchEngine/settings.py' and look for a dictionary named 'DATABASES'. Once you find it, just enter your credentials.
5. Open a terminal and enter ``` python manage.py makemigrations   ``` to create a migration and then migrate it to the database using ```  python manage.py migrate  ```.
6. Open django shell using ```  python manage.py shell  ```.
7. Declare a seed_url variable that stores the url of the seed page. Then add it to the crawl frontier by first importing the crawl frontier model using ``` from WebCrawler.models import CrawlFrontier ``` and then using ``` CrawlFrontier.objects.create(url=seed_url) ```.
8. To run the web crawler, import the run_webCrawler function from WebCrawler.utils and then execute it.
9. Once the web crawler is done with its job, exit the django shell and enter ``` python manage.py runserver ``` to start up the django server.

# Notes
Crawling the web is a Tremendous and Resource intensive task. Therefore, to keep the
    project feasible, I decided to have the Web Crawler work on a handful of static
    websites I made as a sort of sample mini web.
    The sites of this sample web were hosted using IBM Cloud Object Storage with the
    Seed page having the url (https://sites.s3.jp-tok.cloud-object-storage.appdomain.cloud/seed.html).
    
    Since resources created using the free, IBM Cloud lite account are deleted after about a month of
    inactivity, the sample web may not be there in future.