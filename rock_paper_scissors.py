import random

print("<----------Welcome to Rock Paper Scissors Game---------->")
print("")
def start():
    user=input("Player enter your name:-  ")
    print("____________________________________________________")
    
    list=["rock","paper","scissors"]
    while True:
        cchoice=random.choice(list)
        print("____________________________________________________")
        userchoice=input("Enter your choice as (rock/paper/scissors :-)")
        print("____________________________________________________")
        print(f"you chose {userchoice} and computer chose {cchoice}")
        print("")
        if cchoice==userchoice:
            print("both chose same ,Match draw")
            print("____________________________________________________")
        if cchoice=="rock" and userchoice=="paper":
            print(f"paper cover the rock,{user}  WON")
            print("____________________________________________________")
        elif cchoice=="rock" and userchoice=="scissors":
            print("Rock shmashes the Scissors,Computer WON")
            print("____________________________________________________")
        elif cchoice=="paper" and userchoice=="rock":
            print("Paper cover the rock ,COMPUTER WON")
            print("____________________________________________________")
        elif cchoice=="paper" and userchoice=="scissors":
            print(f"Scissors cut the paper , {user} WON")
            print("____________________________________________________")
        elif cchoice=="scissors" and userchoice=="rock":
            print(f"Rock brakes the Scissors , {user} WON")
            print("____________________________________________________")
        elif cchoice=="scissors" and userchoice=="paper":
            print("Scissors cut the paper, COMPUTER WON")
            print("____________________________________________________")
        elif userchoice=="exit":
            print("Game Over")
            break
start()