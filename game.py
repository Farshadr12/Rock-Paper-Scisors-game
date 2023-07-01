import random
choices = ["rock", "paper", "scisors"]
results = [0, 0]
print("""Welcome to RPS game 
choose your option!""")
while True:
    
    playerChoice = input(">> ").lower()
    comChoice = random.choice(choices)
    if playerChoice == "exit":
        break
    if playerChoice not in choices and playerChoice != "exit":
        print("""Error !! Select one of the options 
1-rock 
2-paper 
3-scisors""")
    elif playerChoice in choices:
        if playerChoice == comChoice:
            print("Its a draw !! let's do it again!")
        elif playerChoice == "rock" and comChoice == "paper":
            results[1] += 1
            print(f"you Lost, Computer was {comChoice}. The Result is ({results})")
        elif playerChoice == "rock" and comChoice == "scisors":
            results[0] += 1
            print(f"you Win, Computer was {comChoice}. The Result is ({results})")
        elif playerChoice == "paper" and comChoice == "rock":
            results[0] += 1
            print(f"you Win, Computer was {comChoice}. The Result is ({results})")
        elif playerChoice == "paper" and comChoice == "scisors":
            results[1] += 1
            print(f"you Lost, Computer was {comChoice}. The Result is ({results})")
        elif playerChoice == "scisors" and comChoice == "rock":
            results[1] += 1
            print(f"you Lost, Computer was {comChoice}. The Result is ({results})")
        elif playerChoice == "scisors" and comChoice == "paper":
            results[0] += 1
            print(f"you Win, Computer was {comChoice}. The Result is ({results})")
        print(f"The Results are ({results}). Wanna play again?")
        stat = input("enter to continue or type no >> ").lower()
        if stat == "no":
            break
    
print("Thank you for playing")