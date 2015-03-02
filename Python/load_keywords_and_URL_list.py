'''
This file is to contain a function for loading the source URL list and search keywords from a file.
input:          filename
output:         data structures containing URL list and search keywords list
'''

def load_source_list(filename):
	if not filename.lower().endswith('.txt'):
		# Needs to handle error without printing
		print "Only .txt files are allowed."
		return

	text_file_string = open(filename, 'r').read()
	source_list = text_file_string.splitlines()
	return source_list