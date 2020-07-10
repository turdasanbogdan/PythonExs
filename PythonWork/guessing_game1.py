from random import randint

number = input("test your luck: ")
number = int(number)
i= randint(1,9)

if number == i:
    print("Lucky bastard")
elif number - i < 0:
    print("you were too low with: " + str(abs(number-i)))
else :
    print("you were to high with: " + str(number-i))        
print(i)    