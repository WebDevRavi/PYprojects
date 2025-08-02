import random
print("Welcome to roll the dice game")
# playing = input("Enter y/n to continue").lower

# while playing == "y":
#     playing = input("Enter y/n to continue").lower
#     print(random.randrange(0,7),random.randrange(0,7))
    
# else:
    # print("Enter Valid Syntax")
    
import random

playing = input("Enter y/n to continue: ").lower()

while playing == "y":
    print("You rolled:", random.randint(1, 6), "and", random.randint(1, 6))
    playing = input("Enter y/n to continue: ").lower()

if playing != "n":
    print("Enter Valid Syntax")

print("Thanks For Playing!")