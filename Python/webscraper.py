'''
This file is to contain the driving program flow for the entire program per the Web Scrape Design documentation.
input:          the name of a configuration file containing a list of source URLs and a list of keywords for searching
output:         (to file) a list of article titles and their corresponding URLs
'''

from load_keywords_and_URL_list import loadSourceList

def file_check(filename):
	try:
		f = open(filename)
		f.close()
		return True
	except IOError as e:
		return False	

def request_filename(filetype):
	inputrequest = "Please input the filename that contains the %s list\n" % (filetype)
	file = raw_input(inputrequest)
	while file_check(file) == False:
	 	print "This file does not exist.\n"
	 	file = raw_input(inputrequest)
 	return file

urlFile = request_filename("url")
keywordFile = request_filename("keyword")

urlList = loadSourceList(urlFile)
keywordList = loadSourceList(keywordFile)

print urlList
print keywordList
