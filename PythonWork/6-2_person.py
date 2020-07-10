person = {
	'first_name' : 'Alin',
	'last_name'  : 'Mircea',
	'age'        : 21,
	'city'       : 'Orastie',
	
}
print(person)
favorite_numbers = {
	'Alin' : 7,
	'Dan'  : 4,
	'Pique': 3,
	'Xavi' : 6,
}
print(favorite_numbers)
for key, value in person.items():
	print("\nKey: " + key +"\nValue: " + str(value) )

for key in favorite_numbers :
    print(key.title())	

friends = ['Alin', 'Pique']

for name in favorite_numbers.keys() :
    print(name.title())

    if name in friends:
       print("Hei, "+ name.title()+" I see your fav number is: " + str(favorite_numbers[name]))     
favorite_languages = {
	'jen'   : 'C',
	'simon' : 'PHP',
	'bamfi' : 'C',
	'berci' : 'C#', 
}       

for languages in set(favorite_languages.values()):
	print(languages)