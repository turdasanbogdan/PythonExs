def string_invert1(x):
    lista = x.split()
    reverse = ""
    for s in range(len(lista)):
        reverse += lista[-(s+1)] + " "
    return reverse
def string_invert2(x):
    lista = x.split()
    lista.reverse()
    res =  " ".join(lista)            
    return res
string = input("hit mw with a long string ")
print(string_invert1(string))
print(string_invert2(string))
