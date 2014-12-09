response = ""

while "goodbye" not in response:
    response = raw_input('Your turn: ')
    response = response.lower()
    if "hello" in response:
        print "And hello to you"
    elif "goodbye" in response:
        print "See you later"
    elif "your name" in response:
        print "My name is computer"
    else:
        print "Some words"