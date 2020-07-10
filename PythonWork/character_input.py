import datetime
now =datetime.datetime.now()
name = input("Enter your name please")
year = input("Now enter your birth year")
n = input("number of iterations")
nr = int(n)
age =now.year-int(year)
age100 = age+100
i=0
for i in range(int(n)):
 print("You will be " + str(age100) + " in 100 years") 
 