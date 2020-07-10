for value in range(1,21):
 print(value)
one_milion_list=list(range(1,10**6+1)) 
print(max(one_milion_list))
three_list=list(range(0,31,3))
for x in three_list:
	print(x)
cubes=[value**3 for value in range(1,11)]
print(cubes)	
powers_of_two=[2**x for x in range(1,26)]
print(max(powers_of_two))
#Sliceing lists
players=['carol', 'martina', 'buendia']
print(players[-2:])
#Copying a list
my_food=['mac&cheese', 'pizza', 'burgers']

mom_food=my_food[:]
mom_food.append('branza')

my_food.pop()
my_food.append('pretzel')
print(my_food)
print(mom_food)
#Tuples
dimensions=(10,100)
print(dimensions[0])
print(dimensions[1])
dimensions=(5,5)
print(dimensions[0])
print(dimensions[1])
