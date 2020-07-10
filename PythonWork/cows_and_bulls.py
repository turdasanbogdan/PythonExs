from random import randint
def compare_numbers(nr,real):

    cows_bulls = [0,0]
    for i in range(len(nr)):
        if nr[i] == real[i]:
            cows_bulls[0] +=1
        elif nr[i] in real:
            cows_bulls[1] +=1
    return cows_bulls            

if __name__ == "__main__":

    real = str(randint(1000,9999))
    cows_bulls = []
    
    while 1:
        
        nr = input ("test your luck: ")
        if(nr == "exit"):
            break
        cows_bulls = compare_numbers(nr,real)
        print(cows_bulls)
        if cows_bulls[0] == 4:
            print("You lucky bastard")
            break
    print(real)    
    
