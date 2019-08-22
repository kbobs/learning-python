filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for lines in lines:
	pi_string += lines.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
	print("Your burthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
