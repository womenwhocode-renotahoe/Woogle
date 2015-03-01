import unittest
import filecmp
from URLandTitles import URLandTitles
import os

# tests don't necessarily run in order

class TestURLandTitles(unittest.TestCase):

	def setUp(self):
		self.url_list = ["www.google.com", "www.techcrunch.com", "www.engadget.com"]
		self.title_list = ["Google", "Tech Crunch", "Engadget"]
		# expected_csv = ["www.google.com,Google\n",
		# "www.techcrunch.com,Tech Crunch\n",
		# "www.engadget.com,Engadget\n"]

	def tearDown(self):
		os.remove('URLandTitleData.csv')

	def test_write(self):
		URLandTitles(self.url_list, self.title_list)
		self.assertTrue(filecmp.cmp('URLandTitleData.csv', 'test_URLandTitles.csv', True))
	
	# # confirms that in uneven lists, the extra items are ignored
	def test_uneven(self):
		url_list=list(self.url_list)
		url_list.append("www.happywidgets.com")
		URLandTitles(url_list, self.title_list)
		self.assertTrue(filecmp.cmp('URLandTitleData.csv', 'test_URLandTitles.csv', False))	

	# the function doesn't self implode when given an empty list
	def test_empty(self):
		url_list=[]
		URLandTitles(url_list, self.title_list)
		self.assertTrue(filecmp.cmp('URLandTitleData.csv', 'test_emptylist.csv', False))	



	# # TODO: test for special characters (single/double quotes and commas)
	def test_special_characters(self):
		url_list=['http://google.com', 'http://google.com', 'http://google.com']
		title_list=["Google - The 'Search' Engine", "Google, The 'Search' Engine", 'Google - The "Search" Engine']
		URLandTitles(url_list, title_list)
		self.assertTrue(filecmp.cmp('URLandTitleData.csv', 'test_special_characters.csv', True))

if __name__ == '__main__':
	unittest.main()
