rivers ={
	'dunare':  'romania',
	'rhine' :  'franta',
	'seine' :  'franta',  
	'thames'  :  'anglia',
	'nil'   :  'egipt',
	'volga' :  'russia',
	'tibru' : 'italia',
}
print(rivers)

for key, value in rivers.items() :
	print("River: " + key.title() + "runs in " + value.title())
for river in rivers.keys():
	print(river.title())
for country in rivers.values():
	print(country.title())	

