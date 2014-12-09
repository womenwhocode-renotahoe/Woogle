import datetime


def computer_side(human):
	chat = {"hi" : "Hello there.",
		"what time is it" : tell_time(),
		"how is the weather": "Why don't you look out the window?",
		"what is your name": "My name is Arthur, King of the Britons."}
	try:
		print(chat[human])
	except KeyError:
		print("So how about them Giants?")



def tell_time():
	time = datetime.datetime.now()
	return time.strftime('%H:%M')

