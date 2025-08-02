import random

print("You will have to guess the number")
randomnum = random.randrange(1,100)
user_choise = int(input("Guess the Number : "))
count = 0
while user_choise != randomnum:
    if user_choise<randomnum:
        print("Too Low!!")
    elif user_choise>randomnum:
        print("Too high!!")
    user_choise = int(input("Try again :"))
    count = count + 1
else:
    print("Enter Valid number")
    
print(f"You guessed the numner in {count} times")