number = input("Enter a number and I'll tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even")
else:
	print("\nThe number " + str(number) + " is odd")

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
