from random import sample, randint
def eliminate_duplicate(x):
    return list(dict.fromkeys(x))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,13]

a = eliminate_duplicate(a)
b = eliminate_duplicate(b)

c = [el for el in a if el in b]

print(c)
    
