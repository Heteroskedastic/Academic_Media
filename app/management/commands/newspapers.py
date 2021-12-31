import datetime
import logging

import requests
from django.core.management import BaseCommand
from app import models
log = logging.getLogger(__name__)
import newspaper

class Command(BaseCommand):
    help = 'Store API data in system'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--url', type=str, help='Article URL which need to parse', )


    def handle(self, *args, **options):
        try:
            url = options.get('url', None)
            News = {
                'source': 'Nil',
                'author': None,
                'title': None,
                'description': None,
                'url': None,
                'urlToImage': None,
                'publishedAt': None,
                'content': None,
            }

            article = newspaper.Article(url)
            article.download()
            article.parse()
            article.nlp()
            News['source'] = None
            if (type(article.authors) == list):
                News['author'] = ",".join(article.authors)
            elif (type(article.authors)):
                News['author'] = article.authors
            News['title'] = article.title
            News['description'] = article.title[:100]
            News['url'] = url
            News['urlToImage'] = article.top_image
            if (type(article.publish_date) == datetime.datetime):
                News['publishedAt'] = article.publish_date
            News['content'] = article.text

            models.News.objects.get_or_create(**News)
            log.info("URl {}".format(News))
        except Exception as e:
            log.error("Exception : {}".format(str(e)))





# top-headlines
# python manage.py newsapi '/top-headlines'