dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# this doesn't work
#dimensions[0] = 250

dimensions = (200,50)
for dimension in dimensions:
	print(dimension)
	
print("original dimensions")
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
