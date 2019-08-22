name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalise the messages you see."
prompt += "\nWhat is you first name? "

name = input(prompt)
print("\nHello, " + name + "!")

def greet_user():
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")
greet_user('jesse')

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	print("(enter q at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name ==  'q':
		break
formatted_name = get_formatted_name(f_name, l_name)
print ("\nHello, " + formatted_name + "!")

