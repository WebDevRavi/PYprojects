print("Im here to do math for you ")
operatos = ["+","-","/","*"]
user_choise = input("Enter operator for calculation (+,-,/,*) : ")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if user_choise not in operatos:
    print("Enter valid operator")
elif user_choise == "+" :
    print(f"the sum of two number is:",num1+num2)    
elif user_choise == "-" :
    print(f"the difference of two number is:",num1-num2)    
elif user_choise == "/" :
    print(f"the division of two number is:",num1/num2)    
elif user_choise == "*" :
    print(f"the multiplication of two number is:",num1*num2)    