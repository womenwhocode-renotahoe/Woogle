__author__ = 'tabby'
import Responses

response = ''

while not Responses.is_farewell(response):
    response = raw_input('Your turn: ')
    response = response.lower()
    print Responses.respond(response)
