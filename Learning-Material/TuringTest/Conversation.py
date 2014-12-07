__author__ = 'tabby'
from Responses import respond, is_farewell

response = ''

while not is_farewell(response):
    response = raw_input('Your turn: ')
    response = response.lower()
    print respond(response)
