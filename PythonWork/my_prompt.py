car= input("What car do you want ?")
print("Let me see if i can find you a " + car.title())

clients = input("How many people in dinner room ?")
nr_clients = int(clients)

if nr_clients >= 8: 
 print("You will have to wait")
else:
 print("Table is ready ;)")

nr= input("While you wait let `s see if next number is div of 10: ")
nr=int(nr)

if nr % 10 == 0: 
	print("IT issss")
else:	
	print("IS nooot :((")
