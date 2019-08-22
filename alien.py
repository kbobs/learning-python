alien_0 = {'colour': 'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])

print(alien_0['colour'])

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

alien_0 = {'colour' : 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['colour'] = 'green'
alien_0['points'] = 5



print(alien_0)

alien_0 = {'colour': 'green'}
print('The alien is ' + alien_0['colour'] + ".")

alien_0['colour'] = 'yellow'
print('The alien is now ' + alien_0['colour'] + ".")

#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print('Original x_position: ' + str(alien_0['x_position'])

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

#if alien_0['speed'] == 'slow':
	#x_increment = 2
#elif alien_0['speed'] == 'medium':
	#x_increment = 2
#else:
	#This must be a fast alien.
	#x_increment = 3

# The new position is the old position plus the increment.

del alien_0['points']
print(alien_0)
