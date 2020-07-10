string = input("da un string ba: ")
string2 = ""

for s in reversed(string):
    string2 = string2+s

print(string2)   

if string == string2:
    print("palindrom")
else :
    print("nu palindrom")     