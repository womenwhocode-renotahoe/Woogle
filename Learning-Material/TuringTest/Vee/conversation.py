import datetime

import statements


while True:
	human = input("Your turn: ").lower()

	if "bye" in human:
		print("Nice chatting with you. Bye.")
		break
	else:
		statements.computer_side(human)

