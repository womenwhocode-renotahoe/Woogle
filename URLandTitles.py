# '''
# This file should contain a function which save the new, valid URLs and article titles to a local file.
# inputs:         new URLs list, article title list
# output:         (to file) new URLs list, article title list
# '''

# test parameters below
# URLList = ["1", "2", "3"]
# TitleList= ["a", "b", "c"]

# expected results
# [(1, 'a'), 
# (2, 'b'), 
# (3, 'c')]

# list(zip()) seems to be for Python 3, you can use zip() in Python 2

# new way using csv module
import csv

def URLandTitles(URLList=['http://google.com'], TitleList=["Google, The 'Search' Engine"]):
	output = zip(URLList, TitleList)
	# return output
	with open("URLandTitleData.csv", "w+b") as f:
		csv_row = csv.writer(f, delimiter = ' ', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
		for line in output:
			csv_row.writerow(line)