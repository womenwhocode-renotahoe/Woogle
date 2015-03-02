'''
This file is to contain the driving program flow for the entire program per the Web Scrape Design documentation.
input:          the name of a configuration file containing a list of source URLs and a list of keywords for searching
output:         (to file) a list of article titles and their corresponding URLs
'''
import os.path
import urllib2
from urlparse import urljoin

from bs4 import BeautifulSoup

from load_keywords_and_URL_list import load_source_list
from parse_web_content import parse_content

def check_file_errors(filename):
 	return not os.path.isfile(filename) or len(load_source_list(filename)) == 0

def webscraper(source_file, keywords_file):
    if check_file_errors(source_file):
        raise OSError("Source file is not valid")
    if check_file_errors(keywords_file):
        raise OSError("Keywords file is not valid")
    urls = load_source_list(source_file)
    keywords = load_source_list(keywords_file)
    found_url_list = []
    found_title_list = []

    for url in urls:
        response = urllib2.urlopen(url)
        article_list = response.read()
        article_list_doc = BeautifulSoup(article_list)
        for link in article_list_doc.find_all('a'):
            article_url = link.get('href')
            if not article_url.startswith("http"):
                article_url = urljoin(url, article_url)
            try:
                article_response = urllib2.urlopen(article_url)
                article_content = article_response.read()
                if parse_content(keywords, article_content):
                    print "%s matches keywords" % article_url
                    found_url_list.append(article_url)
            except urllib2.URLError:
                pass
    # needs to import url and title csv maker thing