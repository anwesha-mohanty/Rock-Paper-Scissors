#A simple rock paper scissors game
import random
print("The rules are:")
print("Rock vs Paper- Paper wins")
print("Rock vs scissors- Rock wins")
print("Paper vs Scissors- Scissors win")
userScore=0
compScore=0
ch=0
while 1:
    print("Your turn")
    print("Enter choice:")
    print("1.Rock\t2.Paper\t3.Scissors")
    ch=int(input())
    while ch>3 or ch<1:
        print("Enter valid input")
        ch=int(input())
    print("You chose:")
    if ch==1:
        print("Rock")
    if ch==2:
        print("Paper")
    if ch==3:
        print("Scissors")      
    print("\nComputer's turn")
    comp_ch=random.randint(1,3)
    while ch==comp_ch:
        comp_ch=random.randint(1,3)
    print("Computer chose:")
    if comp_ch==1:
        print("Rock")
    if comp_ch==2:
        print("Paper")
    if comp_ch==3:
        print("Scissors")
    if ch==1 and comp_ch==2 or ch==2 and comp_ch==1:
        res=2
    elif ch==2 and comp_ch==3 or ch==3 and comp_ch==2:
        res=3
    else:
        res=1
    if ch==res:
        print("\nYou win!")
        userScore+=1
    else:
        print("\nComputer wins!")
        compScore+=1
         
    print("\nDo you want to play again?[y/n]")
    repeat=input()
    if repeat=="n" or repeat=="N":
        break
    else:
        continue

print("Your score={}".format(userScore))
print("Computer\'s score={}".format(compScore))

print("Thank you for playing!")
