sandwich_orders=['pui','vita', 'pastrami','paine', 'pastrami', 'pastrami']
finished_sandwiches=[]

print("We ran out of pastrami")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
while sandwich_orders :
	finished = sandwich_orders.pop()
	finished_sandwiches.append(finished)
print(finished_sandwiches)
print(sandwich_orders)	

responses = {}

quit=""
while quit != "x":
	name=input("Whats`s your name? ")
	nation = input("Where are you from ? ")

	responses[name] = nation

	quit=input("To continue the poll prex any key, else pres x")


print("responses" + str(responses))
print("---------Poll response, got the next countries: -----------")
for country in set(responses.values()):
	print(country)

