import logging

import requests
from django.core.management import BaseCommand
from app import models
log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Store API data in system'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--apiKey', type=str, help='Newsapi apiKey', )
        parser.add_argument('-e', '--endpoint', type=str, help='Enpoint', )
        parser.add_argument('-q', '--query', type=str, help='Query', )
        parser.add_argument('-c', '--country', type=str, help='country', )

    def handle(self, *args, **options):
        try:
            url = 'https://newsapi.org/v2/'
            endpoint = options.get('endpoint', None)
            apiKey = options.get('apiKey', None)
            country = options.get('country', None)
            query = options.get('query', None)
            param = None
            total = 1
            parse = 0
            page = 1

            while parse < total:
                if query:
                    param = url + str(endpoint) + '?q=' + str(query) + '&apiKey=' + apiKey + '&page=' + str(page)
                if country:
                    param = url + str(endpoint) + '?country=' + str(country) + '&apiKey=' + apiKey + '&page=' + str(
                        page)
                log.info("URL : {}".format(param))
                req = requests.get(param)
                log.info("Status code: {}".format(req.status_code))
                articles = req.json().get('articles')
                parse = parse + len(articles)
                page = page + 1
                total = req.json().get('totalResults')
                for i in articles:
                    i['source'] = i.get('source').get('name')
                    models.News.objects.get_or_create(**i)
        except Exception as e:
            log.error("Exception : {}".format(str(e)))





# top-headlines
# python manage.py newsapi '/top-headlines'