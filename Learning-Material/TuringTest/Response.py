__author__ = 'tabby'

NAME = 'Roboto'
AGE = 10000

def is_greeting(phrase):
    if 'hi' in phrase or 'hello' in phrase or 'hey' in phrase:
        return True

def is_state_question(phrase):
    if 'how' in phrase and 'you' in phrase and not 'old' in phrase:
        return True

def is_name_question(phrase):
    if 'name' in phrase and 'what' in phrase:
        return True

def is_age_question(phrase):
    if 'how old' in phrase or 'age' in phrase:
        return True

def is_farewell(phrase):
    if 'bye' in phrase or 'see' in phrase:
        return True

def respond(phrase):
    if is_greeting(phrase):
        return "Hello."
    elif is_state_question(phrase):
        return "I am satisfactory."
    elif is_name_question(phrase):
        return "My name is " + NAME + "."
    elif is_age_question(phrase):
        return "I'm " + str(AGE) + " years old."
    elif is_farewell(phrase):
        return "Goodbye!"
    else:
        return "How about this weather?"