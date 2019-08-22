my_foods = ['pizza', 'falafe;', 'carrot cake']
friend_foods = my_foods[:]
print("My favourite foods are:")
print(my_foods)

print("\My friend's foods are:")

# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream'
print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)
