import unittest
import filecmp
import URLandTitles

# tests don't necessarily run in order

class TestURLandTitles(unittest.TestCase):

	def setUp(self):
		self.url_list = ["www.google.com", "www.techcrunch.com", "www.engadget.com"]
		self.title_list = ["Google", "Tech Crunch", "Engadget"]
		# expected_csv = ["www.google.com,Google\n",
		# "www.techcrunch.com,Tech Crunch\n",
		# "www.engadget.com,Engadget\n"]

	def test_write(self):
		# URLList.append("www.happywidgets.com")
		URLandTitles.URLandTitles(self.url_list, self.title_list)
		self.assertTrue(filecmp.cmp('URLandTitleData.csv', 'test_URLandTitles.csv', False))
	
	# confirms that in uneven lists, the extra items are ignored
	def test_uneven(self):
		self.url_list.append("www.happywidgets.com")
		URLandTitles.URLandTitles(self.url_list, self.title_list)
		self.assertTrue(filecmp.cmp('URLandTitleData.csv', 'test_URLandTitles.csv', False))	

	# the function doesn't self implode when given an empty list
	def test_empty(self):
		self.url_list=[]
		URLandTitles.URLandTitles(self.url_list, self.title_list)
		self.assertTrue(filecmp.cmp('URLandTitleData.csv', 'test_emptylist.csv', False))	

	# TODO: test for special characters (',', '\n')

if __name__ == '__main__':
	unittest.main()
