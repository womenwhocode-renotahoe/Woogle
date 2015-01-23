# '''
# This file should contain a function which save the new, valid URLs and article titles to a local file.
# inputs:         new URLs list, article title list
# output:         (to file) new URLs list, article title list
# '''

URLList = ["1", "2", "3"]
TitleList= ["a", "b", "c"]

# [(1, 'a'), 
# (2, 'b'), 
# (3, 'c')]
output = []
def URLandTitles(URLList, TitleList):
	output = list(zip(URLList, TitleList))
	# return output
	CreateFile = open("URLandTitleData.csv", "w+b")
	for line in output:
		CreateFile.write(", ".join(line)+"\n")
	CreateFile.close()

URLandTitles(URLList, TitleList)