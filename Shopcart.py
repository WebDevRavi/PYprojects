print("This programme is to manage cart and total it")
total_money = 0
cart = []
while True:
    add_item = input("Enter item to be added(q/quit) : ")
    
    if add_item.lower() == "q" or add_item.lower() == "quit":
        print(f"The items are: {cart}")
        for food in cart:
            print(food,end=" ")
        print(f"The total is: ${total_money}")
        break
    try:
        money = int(input("Enter amount of item : "))
        cart.append(add_item)
        total_money = total_money + money
    except:
        print("Enter valid value")
        
