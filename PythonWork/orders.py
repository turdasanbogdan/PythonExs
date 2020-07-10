numbers=list(range(1,10))
print(numbers)
for number in numbers: 
	if number == 1:
			print(str(number)+"st")
	elif number == 2:
			print(str(number)+"nd")
	elif number == 3:
        	print(str(number)+"rd")
	elif number in numbers[4:] :
        	print(str(number)+"th")   
print("Done")         		 		