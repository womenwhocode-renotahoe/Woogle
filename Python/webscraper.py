'''
This file is to contain the driving program flow for the entire program per the Web Scrape Design documentation.
input:          the name of a configuration file containing a list of source URLs and a list of keywords for searching
output:         (to file) a list of article titles and their corresponding URLs
'''
import os.path

from load_keywords_and_URL_list import load_source_list

source_URLs_file = 'urls.txt'
search_keywords_file = 'keywords.txt'

def check_file_errors(filename):
 	return not os.path.isfile(filename) or len(load_source_list(filename)) == 0

def webscraper(source_file, keywords_file):
	if check_file_errors(source_file):
		raise OSError("Source file is not valid")
	if check_file_errors(keywords_file):
		raise OSError("Keywords file is not valid")

	# continue ...