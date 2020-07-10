from random import *
lista = sample(range(1,100), randint(1,100) )
lista2 = [i for i in lista if i % 2 == 0]
print(lista)
print(lista2)