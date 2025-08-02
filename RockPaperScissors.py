import random
print("Welcome to Rock, Paper and Scissors game")
Win_Count = 0

while True:
    Comp_choise = ["r","p","s"]
    comp = random.choice(Comp_choise)
    choise = input("Enter (R/P/S) :").lower()
    
    if choise not in Comp_choise:
        print("Enter valid choise")
        continue
    
    if choise == comp:
        print(f"DRAW!! computer choose: {comp}")
    elif choise == "r" and comp == "p":
        print(f"YOU LOST!!computer choose: {comp}")
    elif choise == "r" and comp == "s":
        print(f"YOU WON!! computer choose: {comp}")
        Win_Count = Win_Count + 1
    elif choise == "p" and comp == "r":
        print(f"YOU WON!! computer choose: {comp}")
        Win_Count = Win_Count + 1
    elif choise == "p" and comp == "s":
        print(f"YOU LOST!! computer choose: {comp}")
    elif choise == "s" and comp == "r":
        print(f"YOU LOST!! computer choose: {comp}")
    elif choise == "s" and comp == "p":
        print(f"YOU WON!! computer choose: {comp}")
        Win_Count = Win_Count + 1
   
    game_continue = input("Do you want to continue? (y/n): ").lower()
    if game_continue != 'y':
        break

print(f"You won {Win_Count} times")