'''
This file is to contain the driving program flow for the entire program per the Web Scrape Design documentation.
input:          the name of a configuration file containing a list of source URLs and a list of keywords for searching
output:         (to file) a list of article titles and their corresponding URLs
'''

from load_keywords_and_URL_list import load_source_list

source_URLs_file = 'urls.txt'
search_keywords_file = 'keywords.txt'

def check_source_file_exists(filename):
	try:
		f = open(filename)
		f.close()
		return True
	except IOError as e:
		return False	

def check_file_errors(filename):
 	if not check_source_file_exists(filename):
		# TO-DO: raise error
		return True

	if len(load_source_list(filename)) = 0:
		# TO-DO: raise error
		return True
	else:
		return False

def webscraper():
	if check_file_errors(source_URLs_file) or check_file_errors(search_keywords_file):
		# TO-DO: raise error
		return

	# continue ...