pets = [{'manz': 'Doru', 'cal' : 'Dan',}, {'catar': 'Dori'}]

for dict in pets :
	for key, val in dict.items():
		print(key.title()+ " is owned by:" + val)


favorite_places = {
	'luigi' : ['La mare', 'Slobozia', 'La Dunare'],
	'simon' : ['Paris', 'Bruxelles', 'Arad'],
	'paul'  : ['Palma de Mallorca', 'Saracie', 'Saracie'],
}		

for name, places in favorite_places.items():
	print(name.title() + " favorite places are :")
	for place in places :
		print(place)




cities = {
	'roma' :
	{
	  'country': 'italia',
	  'population' : '100.000',
	  'fact' : 'they suck at football',
	},

	'london' :
	{
      
       'country' : 'England',
       'population': '150.000',
       'fact' : 'not a fact'


	},
}	


for city, info in cities.items():
	print(city.title()+ "\nInfo: ")
	for key, value in info.items():
		print(key + " :" + value)	