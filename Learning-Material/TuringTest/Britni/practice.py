def start_convo():
	name = raw_input("Hi! What is your name? ")
	print "Welcome, " + name + ". My name is Awesome."
	age = raw_input("How old are you? ")

	if int(age) > 17:
		adult_convo(name, age);
	else:
		kid_convo();

def adult_convo(name, age):
	print "Silly rabbit, Trix are for kids!"
	work = raw_input("Where is your cubicle? ")

	if len(work) > 10:
		print "That sounds complicated ... For a human."
	else:
		print "Congrats ... I guess?"

	print "I know everything about you now! " + name + ", the " + str(age) + "-year-old weirdo that works at " + work + "."

def kid_convo():
	print "Yeah, your life rocks!"

start_convo();