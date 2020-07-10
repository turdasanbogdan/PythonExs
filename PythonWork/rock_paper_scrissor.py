print("Let the games begin!!")
print("Select what type of game you want:")
print("1---> 2 din 3/n 2---> 3 din 5 /n 3---> 5 din 7")
class Player:
    score=0
    choice=""
i = input("alege tipul jocului")
tipuri = [(2,3), (3,5), (5,7)]
winns = [("scrissor", "paper"), ("rock", "scrissor"), ("paper","rock")]
p1 = Player()
p2 = Player()
x=0
i = int(i)
t = tipuri[i-1]

while x != (tipuri[i-1])[1]:
    p1.choice = input("1.your round:")
    p2.choice = input("2.your round dude:")
    tuplu = (p1.choice,p2.choice)
    print(p1.score,p2.score)
    if tuplu in winns :
        p1.score += 1
        x += 1
    tuplu = (p2.choice, p1.choice)
    if tuplu in winns :
        p2.score += 1
        x += 1

if p1.score > p2.score:
    print("fisrt player winns")
else :
    print("2nd player winns")    
print(p1.score,p2.score)
print("Good game guys")        



    
    
    