def remove_duplicates1(x):
    return list(dict.fromkeys(x))
def remove_duplicates2(x):
     s= set()
     for el in x:
         s.add(el)
     return list(s)
 
a=[1,1,1,2,2,2,3,4,5,5,7]
print(remove_duplicates1(a))
print(remove_duplicates2(a))
