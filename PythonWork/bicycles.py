bicycles=['trek', 'connondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1].title())# get the last elem
message= "MY bicycle need a new " + bicycles[0] + " because is not " + bicycles[-1]
print(message)

##Modifying Elemes in a List: Lists are dynamic, i can change them whenever i want
motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0]="kateem"
print(motorcycles)
motorcycles.append("husvarna")
motorcycles.insert(0,"viespe")
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_moto= motorcycles.pop() # it poppes from the final 
print(motorcycles)
print(popped_moto)
popped_moto_index=motorcycles.pop(1) #it poppes the element from index 1
print(motorcycles)
print(popped_moto_index)
#remove by value
new_motors=['honda', 'ducati', 'suzuki', 'yamaha']
removable=['honda', 'suzuki']
new_motors.remove(removable[1])
print(new_motors)
