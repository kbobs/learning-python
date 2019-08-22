squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	print(squares)

("\n")

squares = []
for value in range(1,11):
	squares.append(value**2)
	print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Digits = " + str(digits))
print("Min: " + str(min(digits)) + " Max: " + str(max(digits)) + 
	  " Sum: " + str(sum(digits)))
("\n")
squares = [value**2 for value in range(1,11)]
print(squares)
