'''
This file should contain a function which determines whether the fetched web content is something we'd want.
inputs:         search keyword list, webpage content
output:         good or not good
'''

def parse_content(keywords, content):
    if any(word in content for word in keywords):
        return True
    else:
        return False