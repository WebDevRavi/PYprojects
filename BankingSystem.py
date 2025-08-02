# print("--------------------------------------\nWelcome to Bhartiya International Bank\n--------------------------------------\n1.Show Balance \n2.Deposite\n3.Withdraw\n4.Exit\n**************************************")
# Balance = 0
# #loop
# while True:
#     user_choise = int(input("Enter your choise: "))

#     if user_choise == 1:
#         print(f"Balance : ${Balance}")
#     elif user_choise == 2:
#         depo = int(input("Enter Amount: "))
#         Balance = Balance + depo
#     elif user_choise == 3:
#         with_amount = int(input("Enter Amount: "))
#         if Balance>=with_amount:
#             print(f"Amount Withdrawn ${with_amount} and remaning ${Balance-with_amount}")
#         else:
#             print("Insufficient funds")
#     elif user_choise == 4:
#         print("Thanks for using our bank!!")
#         break

print("--------------------------------------\nWelcome to Bhartiya International Bank\n--------------------------------------\n1.Show Balance \n2.Deposite\n3.Withdraw\n4.Exit\n**************************************")
Balance = 0
#loop

def Show_balance():
    print(f"Balance : ${Balance}")

def Deposite():
    global Balance
    depo = int(input("Enter Amount: "))
    Balance = Balance + depo

def Withdraw_amm():
    global Balance
    with_amount = int(input("Enter Amount: "))
    if Balance >= with_amount:
        Balance -= with_amount  # <- correctly update the balance
        print(f"Amount Withdrawn ${with_amount} and remaining ${Balance}")
    else:
        print("Insufficient funds")

while True:
    user_choise = int(input("Enter your choise: "))

    if user_choise == 1:
        Show_balance()
    elif user_choise == 2:
        Deposite()
    elif user_choise == 3:
        Withdraw_amm()
    elif user_choise == 4:
        print("Thanks for using our bank!!")
        break