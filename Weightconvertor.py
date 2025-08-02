print("This programme is to convert weight into pound or kg")
user_choise = float(input("Enter the weight you wnat to convert : "))
to_convert = int(input("what you wnat to convert\nTo convert Kg to Pound enter 1 \nTo convert Pound to Kg enter 2\nEnter choise :  "))
if to_convert == 1:
    print(f"{user_choise}kg to pound is {user_choise*2.2} Pound")
elif to_convert == 2:
    print(f"{user_choise}pound to kg is {user_choise*0.4} Kg")
else:
    print("Enter valid choise")  