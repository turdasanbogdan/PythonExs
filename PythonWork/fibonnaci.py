def fibonnaci(n):
    fibo= [1,1]
    while n != 1:
        n -=1
        fibo.append(fibo[-1]+fibo[-2])
        
    print(fibo)            

fibonnaci(6)    