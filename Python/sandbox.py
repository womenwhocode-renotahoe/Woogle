__author__ = 'erin'

import requests
import logging

LG_FILENAME = 'webscraper.log'
logging.basicConfig(filename=LG_FILENAME, level=logging.WARN, format='%(asctime)s %(levelname)s %(message)s',)


def webpage_accessor(url='http://www.womenintechnology.org/news-press'):
    response = requests.get(url)

    if response.status_code == 200:
        return response.content
    else:
        logging.warn(url + ' does not return status code 200')