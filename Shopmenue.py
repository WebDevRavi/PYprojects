print("Welcome to the theatre! Here's our menu:\n------- Menu -------\nPizza    : $12\nPasta    : $10\nNachos   : $6\nChips    : $3\nFries    : $7")
dic = {"pizza":12,"pasta":10,"nachos":6,"chips":3,"fries":7}
print(dic.keys())
cart = []
total = 0
while True:
    add_item = input("Enter item to be added(q/quit) : ").lower()
    
    if add_item == "q":
        break
    
    elif dic.get(add_item) is not None:
        cart.append(add_item)
# for i in cart:
#     print(cart,end=" ")
for add_item in cart:
    total += dic.get(add_item)
    print(add_item,end=" ")
print(f"Your total bill is ${total}")
        

    
    