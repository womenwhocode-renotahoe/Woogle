'''
This file is to contain a function for loading the source URL list and search keywords from a file.
input:          filename
output:         data structures containing URL list and search keywords list
'''

def loadSourceList(filename):
	textFile = open(filename, 'r')
	textString = textFile.read()
	sourceList = textString.split('\n')
	print sourceList

loadSourceList('keywords.txt')