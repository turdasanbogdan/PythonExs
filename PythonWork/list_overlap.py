import random
a = random.sample(range(1,100),15)
b = random.sample(range(1,100),15)
print(a)
print(b)
c = []
c= [el for el in a if el in b]
print(c) 