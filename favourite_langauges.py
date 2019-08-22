from collections import OrderDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
	print(name.title() + "'s favourite language is " 
	+ language.title() + ".")

favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
print("Sarah's favourite language is " + favourite_languages['sarah']
.title() + ".")

for name, language in favourite_languages.items():
	print(name.title() + "'s favourite language is " 
	+ language.title() + ".")

for name in favourite_languages.keys():
	print(name.title())

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() + ", I see your favourite language is " + favourite_languages[name].title() + "!")

if 'erin' not in favourite_languages.keys():
	print("Erin, please take our poll!")
	
for name in sorted(favourite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

print("The following languages gave been mentioned: ")
for language in set(favourite_languages.values()):
	print(language.title())
