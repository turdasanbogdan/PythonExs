from divisors import divs

n = input("give number ")
n = int(n)

list = divs(n)
if len(list) > 2:
    print("NOt prime ")
else :
    print("prime")    